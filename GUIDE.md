# GHOSTHAND — Complete Setup Guide
## Your hands are busy. Your AI isn't.

---

## WHAT YOU'RE BUILDING

GHOSTHAND is an AI building mentor with 3 specialist agents:
- **SPOTTER** — watches for safety hazards (proactive alerts)
- **GUIDE** — gives step-by-step building instructions  
- **LOOKUP** — identifies parts and finds specs via Google Search

You talk to it, point your camera at what you're building, and it helps.

---

## BEFORE YOU START

You already have these working (from the PARALLAX setup):
- ✅ Python 3.13
- ✅ Git
- ✅ VS Code
- ✅ Vertex AI credentials (project: parallax-2026)

---

## STEP 1: EXTRACT AND SET UP (3 minutes)

1. Download the `ghosthand-project.tar.gz` file
2. Extract it to your Desktop (right-click → Extract All, or use 7-Zip)
3. You should have: `C:\Users\Admin\OneDrive\Desktop\ghosthand\`

Open VS Code → File → Open Folder → select the `ghosthand` folder.

Open a terminal in VS Code (Terminal → New Terminal).

Run these ONE AT A TIME:

```
python -m venv .venv
```

```
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of your prompt.

```
pip install google-adk google-genai python-dotenv
```

Wait for it to finish (reuses cached packages, should be fast).

---

## STEP 2: CHECK YOUR .ENV FILE (1 minute)

Open `ghosthand\.env` in VS Code (inside the ghosthand subfolder).

Make sure it says:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=parallax-2026
GOOGLE_CLOUD_LOCATION=us-central1
```

If your Google Cloud project has a different name, change `parallax-2026` to match.

---

## STEP 3: RUN IT (1 minute)

Make sure your terminal is in the `ghosthand` folder (the TOP level one, where `requirements.txt` is):

```
cd C:\Users\Admin\OneDrive\Desktop\ghosthand
```

Make sure venv is active (you should see `(.venv)` in prompt):

```
.venv\Scripts\Activate.ps1
```

Run ADK:

```
adk web --no-reload
```

You should see:

```
ADK Web Server started
For local testing, access at http://127.0.0.1:8000.
Uvicorn running on http://127.0.0.1:8000
```

**DO NOT CLOSE THIS TERMINAL. Leave it running.**

---

## STEP 4: USE IT (the fun part)

Open Chrome and go to: **http://localhost:8000**

1. Click the **"Select an agent"** dropdown (top-left)
2. You should see **"ghosthand"** in the list — click it
3. Type: **"Hello, what can you do?"**
4. GHOSTHAND will respond!

### To test with camera:
1. Click the **camera icon** at the bottom
2. Allow camera access
3. Point at something (a tool, electronics, anything)
4. Type: **"What do you see?"**

### Example things to try:
- Point at a screwdriver → "What type of screwdriver is this?"
- Point at a circuit board → "Can you identify these components?"
- Type: "How do I wire a light switch?"
- Type: "What's the pinout for a USB-C connector?"
- Point at wires → "Is this wiring safe?"

---

## TROUBLESHOOTING

| Problem | Fix |
|---------|-----|
| "No agents found" in dropdown | Make sure you ran `adk web --no-reload` from the TOP `ghosthand` folder (where requirements.txt is), NOT from inside `ghosthand/ghosthand/` |
| Terminal shows errors on startup | Check that `ghosthand/.env` has `GOOGLE_GENAI_USE_VERTEXAI=TRUE` |
| "Module not found" error | Make sure `__init__.py` exists and has `from . import agent` |
| Agent doesn't respond | Check terminal for errors. Make sure Vertex AI is working. |
| Camera not working | Make sure you're using Chrome and allowed camera permission |

---

## NEXT STEPS (after it's working)

### Push to GitHub:
```
cd C:\Users\Admin\OneDrive\Desktop\ghosthand
git init
git add .
git commit -m "GHOSTHAND v1.0"
git remote add origin https://github.com/YOUR_USERNAME/ghosthand.git
git push -u origin main
```

### Record demo video (< 4 minutes):
1. Screen record yourself using GHOSTHAND
2. Show it identifying parts, giving safety warnings, guiding a build
3. Upload to YouTube

### Deploy to Cloud Run:
(Requires gcloud CLI — install from https://cloud.google.com/sdk/docs/install)

### Submit on Devpost:
Go to https://geminiliveagentchallenge.devpost.com
Fill in all fields, link your GitHub and YouTube video.

---

## THE KEY THING

Run `adk web --no-reload` from the TOP `ghosthand` folder (where requirements.txt is).
NOT from inside the `ghosthand/ghosthand/` subfolder.

```
ghosthand/              ← extract tar here, run adk web from HERE
├── ghosthand/          ← ADK auto-discovers this as your agent
│   ├── __init__.py
│   ├── agent.py
│   ├── tools.py
│   └── .env
├── requirements.txt
├── README.md
└── GUIDE.md
```

That's it. Go build.
