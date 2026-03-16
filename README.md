# GHOSTHAND

### Your hands are busy. Your AI isn't.

AI-powered building mentor that sees what you're working on and guides you in real-time. Upload a photo of anything - GHOSTHAND identifies it, checks for safety hazards, finds specs, and walks you through step-by-step.

**Category:** Live Agent | **Hackathon:** [Gemini Live Agent Challenge](https://geminiliveagentchallenge.devpost.com/) `#GeminiLiveAgentChallenge`

**Live Deployment:** [https://ghosthand-205219287826.us-central1.run.app](https://ghosthand-205219287826.us-central1.run.app)

---

## Reproducible Testing Instructions

### Prerequisites

- Python 3.11+
- A Google Cloud project with **Vertex AI API** enabled
- `gcloud` CLI installed and authenticated

### Step 1: Clone and install

```bash
git clone https://github.com/Vt01nft/ghosthand.git
cd ghosthand
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\Activate.ps1     # Windows PowerShell
pip install -r requirements.txt
```

### Step 2: Configure your Google Cloud credentials

```bash
gcloud auth application-default login
```

Edit `ghosthand/.env` with your project details:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

### Step 3: Run locally

```bash
adk web --no-reload
```

Open **http://localhost:8000** in Chrome.

### Step 4: Test it

1. Select **ghosthand** from the dropdown (top-left)
2. Click **+ New Session** (top-right)
3. Click the **📎 paperclip** icon next to the message box
4. Upload any photo (a tool, electronic component, wires, anything)
5. Type: **"What is this?"** and press Enter
6. GHOSTHAND will identify objects, read text, and check for safety hazards

### Example test prompts

| Upload | Type this |
|--------|-----------|
| Photo of any tool | "What am I holding?" |
| Photo of wires | "Is this safe to work with?" |
| No photo needed | "How do I wire a basic light switch?" |
| No photo needed | "What's next?" (after a previous instruction) |
| Photo of any component | "What is this and where can I buy one?" |

### Step 5: Deploy to Google Cloud Run (optional)

```bash
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com aiplatform.googleapis.com

gcloud artifacts repositories create ghosthand-repo --repository-format=docker --location=us-central1

gcloud builds submit --tag us-central1-docker.pkg.dev/YOUR_PROJECT/ghosthand-repo/ghosthand:latest

gcloud run deploy ghosthand \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT/ghosthand-repo/ghosthand:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8000 \
  --memory 1Gi \
  --cpu 2 \
  --set-env-vars "GOOGLE_GENAI_USE_VERTEXAI=TRUE,GOOGLE_CLOUD_PROJECT=YOUR_PROJECT,GOOGLE_CLOUD_LOCATION=us-central1"
```

---

## How It Works

Upload a photo of what you're building. GHOSTHAND runs it through 3 specialist agents:

| Agent | Role | Tools | What It Does |
|-------|------|-------|-------------|
| **SPOTTER** | Safety Monitor | `check_safety` | Proactively warns about wrong wiring, exposed components, hazards |
| **GUIDE** | Instructor | `save_progress`, `get_progress` | Step-by-step guidance with progress tracking |
| **LOOKUP** | Parts Expert | `Google Search` | Identifies components, finds specs and prices |

All three coordinate through one orchestrator - like having an experienced mentor looking over your shoulder.

## Architecture

```
User (Browser)
  │
  ├── 📎 Upload photo + type question
  │
  ▼
ADK Web Server (Google ADK)
  │
  ▼
GHOSTHAND Orchestrator (gemini-2.5-flash on Vertex AI)
  ├── SPOTTER (safety)     → check_safety custom tool
  ├── GUIDE (instructions) → save_progress, get_progress custom tools
  └── LOOKUP (parts)       → Google Search tool
  │
  ▼
Google Cloud: Vertex AI (inference) + Cloud Run (hosting)
```

## Tech Stack

- **Agent Framework:** Google ADK (Agent Development Kit)
- **Model:** Gemini 2.5 Flash via Vertex AI
- **Search:** Google Search tool for grounded facts
- **Custom Tools:** Safety checker, progress tracker
- **Deployment:** Google Cloud Run + Artifact Registry + Cloud Build
- **Language:** Python 3.11+

## Google Cloud Services Used

| Service | Purpose |
|---------|---------|
| **Vertex AI** | Gemini 2.5 Flash model inference |
| **Cloud Run** | Application hosting |
| **Artifact Registry** | Docker container storage |
| **Cloud Build** | CI/CD pipeline for building containers |

## Project Structure

```
ghosthand/
├── ghosthand/           # ADK agent package
│   ├── __init__.py      # Package init (from . import agent)
│   ├── agent.py         # 3 sub-agents + orchestrator
│   ├── tools.py         # check_safety, save_progress, get_progress
│   └── .env             # Vertex AI config
├── Dockerfile           # Cloud Run container
├── requirements.txt     # Python dependencies
├── README.md
└── .gitignore
```

## Key Design Decisions

1. **Tool separation**: Each sub-agent has only one tool type (custom OR Google Search) to comply with Gemini's tool-mixing constraints.
2. **No tools on orchestrator**: The root agent only has `sub_agents`, no direct tools - preventing routing conflicts.
3. **Safety-first routing**: SPOTTER checks every image before other agents respond.
4. **Gemini 2.5 Flash**: Chosen for speed - responds in 2-5 seconds with full vision understanding.

## License

MIT

---

*Built by [vt](https://github.com/Vt01nft) for the Gemini Live Agent Challenge. March 2026.*

*This project was created for the purposes of entering the Gemini Live Agent Challenge hackathon. #GeminiLiveAgentChallenge*
