🦷 Dental Doctor Appointment System — Agentic AI
```

A multi-agent AI system for managing dental appointments using LangGraph, Groq LLM, FastAPI, and Streamlit.

The system allows users to interact with a conversational AI assistant to:

Check available appointment slots

Book dental appointments

Cancel appointments

Reschedule appointments

This project demonstrates Agentic AI architecture, where specialized agents collaborate under a Supervisor Agent to complete tasks.
```
🚀 Features
```

🗓️ View available appointment slots

👨‍⚕️ Find doctors by specialization

📅 Book appointments via natural language

❌ Cancel existing bookings

🔄 Reschedule appointments

🤖 Multi-agent orchestration with LangGraph

🌐 FastAPI backend for AI agent execution

💬 Streamlit chat interface for user interaction

📊 CSV-based storage (lightweight database)
```

🧠 Architecture
```
The system follows a Supervisor-Agent architecture.

                    ┌──────────────┐
                    │   Supervisor │
                    │ Intent Router│
                    └──────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   ┌─────────────┐ ┌─────────────┐ ┌───────────────┐
   │ Info Agent  │ │   Booking   │ │  Cancellation │
   │             │ │    Agent    │ │    Agent      │
   └─────────────┘ └─────────────┘ └───────────────┘
          │
          ▼
   ┌───────────────┐
   │ Rescheduling  │
   │     Agent     │
   └───────────────┘
```
⚙️ Technology Stack
```
Component	Technology
Agent Framework	LangGraph
LLM	Groq (Llama 3.3 70B)
AI Toolkit	LangChain
Backend API	FastAPI
Frontend UI	Streamlit
Data Storage	CSV
Data Processing	Pandas
Validation	Pydantic
```
📂 Project Structure
```
Dental-Doctor-Appointment-System--Agentic-AI
dental_agent_project/
├── main.py                          # Entry point - interactive CLI
├── doctor_availability.csv          # Data store for appointments
├── requirements.txt                 # Python dependencies
├── dental_agent/
│   ├── agent.py                     # Main agent definition & tools
│   ├── config/
│   │   └── settings.py              # Configuration & environment
│   ├── models/
│   │   └── state.py                 # State schema definitions
│   ├── tools/
│   │   ├── csv_reader.py            # Read operations (query tools)
│   │   └── csv_writer.py            # Write operations (mutation tools)
│   ├── agents/
│   │   ├── supervisor.py            # Intent classification & routing
│   │   ├── info_agent.py            # Information queries
│   │   ├── booking_agent.py         # Appointment booking
│   │   ├── cancellation_agent.py    # Appointment cancellation
│   │   └── rescheduling_agent.py    # Appointment rescheduling
│   └── workflows/
│       └── graph.py                 # LangGraph workflow definition
```
🛠 Installation
```
1️⃣ Clone the repository
```
git clone https://github.com/MedisettiVinay0519/Dental-Doctor-Appointment-System--Agentic-AI.git
cd Dental-Doctor-Appointment-System--Agentic-AI
```
2️⃣ Create virtual environment
```
python -m venv venv
```
Activate it

Windows
```
venv\Scripts\activate
```
Mac/Linux
```
source venv/bin/activate
```
3️⃣ Install dependencies
```
pip install -r requirements.txt
```
4️⃣ Configure environment variables
```
Create .env

GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0
```
▶️ Running the System
```
Option 1 — CLI Mode
python main.py
Option 2 — Run FastAPI Backend
uvicorn api:app --reload
```
API documentation:
```
http://127.0.0.1:8000/docs
Option 3 — Run Streamlit UI
streamlit run streamlit_app.py

Streamlit UI:

http://localhost:8501
```
💬 Example Queries
```
View available slots
Show available slots for orthodontist
Book appointment
Book patient 1000082 with Kevin Anderson on 02/09/2026 09:00
Cancel appointment
Cancel appointment for patient 1000082 at 02/09/2026 09:00
Reschedule appointment
Reschedule patient 1000082 from 02/09/2026 09:00 to 03/09/2026 10:00
```
📊 Data Model
```
Appointment data is stored in doctor_availability.csv

Field	Description
date_slot	Appointment date and time
specialization	Dentist specialization
doctor_name	Dentist name
is_available	Slot availability
patient_to_attend	Patient ID
```
🎓 Learning Concepts
```
This project demonstrates:

Agentic AI systems

LangGraph multi-agent orchestration

LLM tool calling

Supervisor-agent architecture

FastAPI backend integration

Streamlit AI interfaces
```
📈 Future Improvements
```
React frontend

PostgreSQL database

Docker deployment

Multi-clinic scheduling

Real-time notifications
```
📜 License
```
This project is intended for educational and research purposes.

✅ This version makes your project look like a serious AI engineering project.

If you want, I can also help you add 3 things that will massively boost this repo on GitHub (stars + recruiter attention).
