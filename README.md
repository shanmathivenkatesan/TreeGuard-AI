# TreeGuard AI 🌳🤖

## Problem Statement
Cities experience only about 47% survival of newly planted trees because post-planting care is inconsistent, understaffed, and poorly monitored. Community involvement exists but lacks structure, leaving trees vulnerable during their most critical early years.

## Solution Description
TreeGuard AI leverages AI, automation, and community engagement to monitor tree health and provide actionable insights:
- Leaf Image Classification for disease detection
- Tree Risk Prediction Model for safety assessment
- Voice & Text Agents for interaction
- Automated Alerts & Escalation workflows

## Agent Workflow
1. User uploads leaf images or tree data.
2. AI agent classifies tree health and predicts risk.
3. Alerts are triggered via automation scripts (n8n).
4. Users receive insights through web/mobile app.

![Agent Workflow Diagram](docs/agent_workflow.png) 

## Tech Stack Used
- **Frontend:** React (Web) / Flutter (Mobile)
- **Backend:** FastAPI (Python)
- **ML Models:** Leaf Classifier, Tree Risk Predictor
- **Agents & Automation:** LangFlow (RootSense, Voice, Match, Gratitude), n8n
- **Database:** Firebase / PostgreSQL
- **APIs:** OpenAI, gTTS




## Key Features
- Real-time tree health monitoring using AI
- Automated risk alerts & escalation
- Voice-enabled feedback system
- Community-friendly web & mobile interface
- Scalable architecture for smart cities

## System Architecture
TreeGuard AI follows a micro-service based architecture:

- Frontend: User uploads tree / leaf data
- Backend: FastAPI handles requests
- ML Models: Predict tree health & risk
- Agents: Process logic & communication
- Automation: n8n triggers alerts
- Database: Stores tree & user records

## Project Impact
- Prevents tree-fall accidents
- Reduces manual inspection effort
- Improves city safety
- Creates environmental awareness

## Future Enhancements
- Drone-based tree scanning
- GPS-enabled tree mapping
- Mobile app with push notifications
- Multilingual voice assistant

## Prototype

Figma UI Prototype:  
👉 https://daily-koala-69081639.figma.site


## Demo Video
https://drive.google.com/file/d/1UIO7lZR6smRmh7PqvL3TNL--URNiZHSK/view?usp=drivesdk


## Setup & Execution Steps

### 1. Clone Repository
```bash
git clone https://github.com/shanmathivenkatesan/TreeGuard-AI.git
cd TreeGuard-AI

### 2. Backend Setup
cd src/backend
pip install -r requirements.txt
uvicorn main:app --reload

### 3. Frontend Setup
cd ../frontend
npm install
npm start

### 4. Run Agents
cd ../agents
python RootSenseAgent.py
python MatchAgent.py
python VoiceAgent.py
python GratitudeAgent.py
