# 🤖 AI Job Application Agent
### ASU AI in Business Club Workshop

A Streamlit web app that acts as an AI agent to help you tailor your resume and generate cover letters for any job posting.

---

## 🚀 How to Run This App

### Option 1: Run Locally (Recommended for Workshop)

1. **Make sure Python is installed**
   - Download from python.org if needed

2. **Install the required libraries**
   Open your terminal and run:
   ```
   pip install streamlit google-generativeai PyPDF2 requests beautifulsoup4
   ```

3. **Run the app**
   Navigate to the folder where app.py is saved, then run:
   ```
   streamlit run app.py
   ```
   The app will open automatically in your browser at http://localhost:8501

---

### Option 2: Deploy Free on Streamlit Cloud (Share with the whole club)

1. Upload app.py and requirements.txt to a GitHub repository
2. Go to share.streamlit.io
3. Connect your GitHub repo
4. Deploy — you get a public URL to share with everyone!

---

## 🔑 Getting Your Free Gemini API Key

1. Go to aistudio.google.com
2. Sign in with your Google account
3. Click "Get API Key"
4. Create a new key — it's completely free!

---

## 💡 What the Agent Does

1. **Accepts your resume** as a PDF upload
2. **Scrapes the job posting** from a URL automatically
3. **Asks you follow-up questions** to personalize the output
4. **Generates:**
   - Match score with strengths and gaps
   - 6 tailored resume bullet points
   - 3 different cover letter versions (different tones)
5. **Lets you download** everything

---

## 🛠 Tech Stack
- Python
- Streamlit (web app framework)
- Google Gemini API (AI)
- PyPDF2 (PDF reading)
- BeautifulSoup (web scraping)

---
*Built for ASU AI in Business Club*
