# GHOSTHAND

### your hands are busy. your AI isn't.

AI-powered hands-free building mentor that sees what you're working on through your camera and guides you in real-time.

**Category:** Live Agent | **Hackathon:** [Gemini Live Agent Challenge](https://geminiliveagentchallenge.devpost.com/) `#GeminiLiveAgentChallenge`

---

## What It Does

Point your camera at what you're building. GHOSTHAND watches and helps:

| Agent | Role | What It Does |
|-------|------|-------------|
| **SPOTTER** | Safety Monitor | Proactively warns about wrong wiring, exposed components, hazards |
| **GUIDE** | Building Instructor | Step-by-step guidance, tracks your progress, knows what's next |
| **LOOKUP** | Parts Expert | Identifies components, finds specs/datasheets via Google Search |

**Key features:** Proactive safety alerts without being asked. Progress tracking across the session. Google Search grounding for specs and manuals. Natural mentor persona.

## Quick Start

```bash
pip install -r requirements.txt
adk web --no-reload
```

Open http://localhost:8000 → select `ghosthand` → start chatting + send camera images.

## Tech Stack

Google ADK 1.26 · Gemini 2.5 Flash · Google Search · Vertex AI · Cloud Run

## Google Cloud Services

Vertex AI (inference) · Cloud Run (hosting) · Artifact Registry (containers) · Cloud Build (CI/CD)

---

*Built by vt for the Gemini Live Agent Challenge. March 2026.*
