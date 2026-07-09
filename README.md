# AI Study Assistant

A Streamlit web app that helps students turn messy notes into a weekly study plan,
draft email replies, and summarize tasks from a pasted syllabus — using Google's
Gemini API.

## Problem
Students often have messy notes, unclear deadlines scattered across syllabi, and
little time to draft replies to professors or classmates. This tool turns unstructured
text into organized, actionable output in seconds.

## Features
- **Notes → Weekly Study Plan**: paste messy notes, get a structured 7-day plan as a table
- **Email Reply Drafts**: describe a situation, get 3 draft replies (formal/casual/brief)
- **Syllabus Task Summarizer**: paste a syllabus or assignment list, get a clean table of tasks and deadlines

## Screenshot
*(add a screenshot here once you have one — see below)*

## How to Run Locally

1. Clone the repo

    git clone https://github.com/TanishaShah1/AI-study-assistant.git
    cd AI-study-assistant

2. Create and activate a virtual environment

    python -m venv venv
    venv\Scripts\activate

3. Install dependencies

    pip install -r requirements.txt

4. Add your Gemini API key
   - Copy `.env.example` to `.env`
   - Get a free key at https://aistudio.google.com/apikey
   - Paste it into `.env`

5. Run the app

    streamlit run app.py

## Sample Prompts / Example Use
**Notes input:** "midterm on chapter 3-5 next friday, also need to finish lab report, professor mentioned photosynthesis will be heavily tested"

**Output:** a 7-day table balancing review of chapters 3-5, lab report time, and extra photosynthesis review.

## Responsible Use & Limitations
- This tool uses a general-purpose AI model (Gemini) and can make mistakes — always double-check generated study plans and deadlines against your actual syllabus.
- The AI is instructed not to invent deadlines or facts, but it can still misread ambiguous or poorly formatted text — verify anything time-sensitive.
- **Privacy:** any text you paste (notes, syllabus, email content) is sent to Google's Gemini API for processing. Avoid pasting sensitive personal information, other people's private messages, or confidential content.
- This is a learning project, not a production tool — no data is stored, but also no security auditing has been done beyond basic API key protection.

## Tech Stack
Python, Streamlit, Google Gemini API, python-dotenv
