# GHOSTHAND

### Your hands are busy Your AI isn't

AI-powered building mentor that sees what you're working on and guides you in real-time. Point your camera at anything - GHOSTHAND identifies it, checks for safety hazards, finds specs, and walks you through step-by-step.

**Category:** Live Agent | **Hackathon:** [Gemini Live Agent Challenge](https://geminiliveagentchallenge.devpost.com/)

---

## How It Works

Upload a photo of what you're building. GHOSTHAND runs it through 3 specialist agents:

| Agent | Role | What It Does |
|-------|------|-------------|
| **SPOTTER** | Safety Monitor | Proactively warns about wrong wiring, exposed components, hazards |
| **GUIDE** | Instructor | Step-by-step guidance with progress tracking |
| **LOOKUP** | Parts Expert | Identifies components, finds specs and prices via Google Search |

All three coordinate through one natural voice - like having an experienced mentor looking over your shoulder.

## Demo

![GHOSTHAND identifying a voltage tester](https://via.placeholder.com/800x400?text=Demo+Screenshot)

> *"You're holding a Voltage Tester - the GERMANY 220-250V marking means it detects AC voltage in the 220-250 volt range. You also have keys on a ROYALTON keyring."*

## Quick Start

### Prerequisites
- Python 3.11+
- Google Cloud account with Vertex AI enabled

### Setup

```bash
git clone https://github.com/Vt01nft/ghosthand.git
cd ghosthand
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\Activate.ps1     # Windows PowerShell
pip install -r requirements.txt
```

### Configure

Create `ghosthand/.env`:
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

Authenticate:
```bash
gcloud auth application-default login
```

### Run

```bash
adk web --no-reload
```

Open http://localhost:8000 → select **ghosthand** → click 📎 to attach a photo → type your question.

## Architecture

```
User (Browser)
  │
  ├── 📎 Upload photo + type question
  │
  ▼
ADK Web Server (adk web)
  │
  ▼
GHOSTHAND Orchestrator (gemini-2.5-flash)
  ├── SPOTTER (safety check) ← check_safety tool
  ├── GUIDE (instructions) ← save_progress, get_progress tools
  └── LOOKUP (parts expert) ← Google Search tool
  │
  ▼
Vertex AI (Gemini 2.5 Flash) on Google Cloud
```

## Tech Stack

- **Agent Framework:** Google ADK 1.26 (Agent Development Kit)
- **Model:** Gemini 2.5 Flash via Vertex AI
- **Search:** Google Search tool for grounded facts
- **Custom Tools:** Safety checker, progress tracker
- **Deployment:** Google Cloud Run
- **Language:** Python 3.11+

## Google Cloud Services Used

- **Vertex AI** - Gemini model inference
- **Cloud Run** - Application hosting
- **Artifact Registry** - Container storage
- **Cloud Build** - CI/CD pipeline

## Project Structure

```
ghosthand/
├── ghosthand/           # ADK agent package
│   ├── __init__.py      # Package init
│   ├── agent.py         # 3 sub-agents + orchestrator
│   ├── tools.py         # Safety checker, progress tracker
│   └── .env             # Vertex AI config
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

## Examples

| You show | You ask | GHOSTHAND says |
|----------|---------|---------------|
| Voltage tester | "What's in my hand?" | "That's a voltage tester rated for 220-250V AC. The GERMANY marking means it's European standard." |
| Tangled wires | "Is this safe?" | "Heads up - those exposed copper ends could short. Wrap them with electrical tape before reconnecting." |
| Circuit board | "What component is this?" | "That's a 470μF electrolytic capacitor. Make sure the negative stripe faces the minus terminal." |
| Any project | "What's next?" | Checks your saved progress and tells you the next step |

## License

MIT

---

*Built by [vt](https://github.com/Vt01nft) for the Gemini Live Agent Challenge. March 2026.*

*This project was created for the purposes of entering the Gemini Live Agent Challenge hackathon. #GeminiLiveAgentChallenge*
