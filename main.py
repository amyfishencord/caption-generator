import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

# Load the API key from an environment variable.

API_KEY = os.environ.get("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GOOGLE_API_KEY is not set. Set it before starting the server "
        "(see the .env file / export instructions)."
    )

client = genai.Client(api_key=API_KEY)

app = FastAPI()


# CORS: by default, a browser blocks a webpage from
# calling a server on a different address/port than
# itself. Since HTML file and this backend run
# on different "origins" while developing, we have to
# explicitly allow it.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # fine for local dev
    allow_methods=["*"],
    allow_headers=["*"],
)



# defines SHAPE of the request the frontend
# will send us. FastAPI uses this to automatically
# validate incoming requests.

class CaptionRequest(BaseModel):
    product: str
    tone: str
    platform: str
    count: int



# The endpoint itself. "@app.post" means: when a POST
# request arrives at /generate-captions, run this
# function. This replaces the fetch() call that used
# to go straight to Gemini from the browser.

@app.post("/generate-captions")
def generate_captions(req: CaptionRequest):
    prompt = (
        f"Write {req.count} short, {req.tone.lower()} marketing captions for "
        f"{req.platform}, advertising: {req.product}. Return ONLY the captions, "
        f"one per line, no numbering, no quotation marks, no extra commentary."
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
    except Exception as e:
        # Surface a clean error to the frontend instead of a raw stack trace
        raise HTTPException(status_code=502, detail=f"Gemini request failed: {e}")

    text = response.text or ""
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    if not lines:
        raise HTTPException(status_code=502, detail="No captions came back from Gemini.")

    return {"captions": lines}



# A simple health check, useful for confirming the
# server is up before wiring the frontend to it.

@app.get("/")
def root():
    return {"status": "caption generator backend is running"}
