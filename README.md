# Caption Press

An AI marketing caption generator that started as a 10-line teaching script and became a small full-stack app.

## The story

This started as a hands-on exercise I led for the AI in Business Club at ASU — a workshop teaching students how to get a free Google Gemini API key and make their first API call. The original notebook is included in this repo (`AI_Marketing_Captions_Workshop_Personal_.ipynb`): a single Python cell that takes a product name and returns three marketing captions.

Afterward, I took that same idea and built it out into a real, deployed application, using the exercise as a jumping-off point to learn the pieces a script like that skips over:

- **Turned the script into a UI** — a browser-based frontend so anyone can use it without touching code, with controls for tone, platform, and caption count.
- **Identified a security problem in my first version** — the initial build called the Gemini API directly from the browser, which meant the API key was visible to anyone inspecting the page. 
- **Built a backend to fix it** — added a small FastAPI server in Python that holds the API key server-side and exposes a single endpoint (`/generate-captions`) for the frontend to call instead. The key never reaches the browser.
- **Debugged the full stack along the way** — including a retired model ID, a Google Cloud project needing the Gemini API explicitly enabled, and Gemini's own transient rate limiting — all while getting comfortable with Git/GitHub for the first time.

## Architecture

```
Frontend (HTML/CSS/JS)  →  Backend (FastAPI, Python)  →  Gemini API
   caption-generator.html         main.py
```

## Running it locally

**1. Install backend dependencies:**
```
pip3 install -r requirements.txt
```

**2. Set your Gemini API key** (get one free at [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)):
```
export GOOGLE_API_KEY="your_key_here"
```

**3. Start the backend:**
```
uvicorn main:app --reload
```

**4. Open `caption-generator.html`** in your browser. It talks to the backend at `http://127.0.0.1:8000`.

## What I'd do next

- Add authentication and rate limiting before letting this run publicly
- Persist generated captions to a database
- Deploy the backend somewhere reachable outside localhost (e.g. Render/Railway) instead of running it locally
