🦷 Dental Appointment Management System (Agentic AI)

A multi-agent AI system for managing dental appointments using LangGraph and Groq LLMs.
The system allows users to interact with a conversational assistant to view available slots, book appointments, cancel bookings, and reschedule visits.

This project demonstrates Agentic AI architecture, where specialized AI agents collaborate under a Supervisor agent to complete tasks.

🚀 Features

🗓️ Check available appointment slots

👨‍⚕️ View doctors by specialization

📅 Book dental appointments

❌ Cancel existing appointments

🔄 Reschedule appointments

🤖 Multi-agent orchestration using LangGraph

💬 Natural language interaction

📊 CSV-based data storage (no database required)

🧠 Architecture

The system uses a Supervisor-Agent pattern where a central coordinator routes requests to specialized agents.

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
   │  Reschedule   │
   │     Agent     │
   └───────────────┘
🧩 Agent Responsibilities
Supervisor Agent

Classifies user intent

Routes request to the correct agent

Info Agent

Handles:

Available slots

Doctor schedules

Patient appointment lookup

Booking Agent

Handles:

Appointment booking

Slot validation

Patient-doctor matching

Cancellation Agent

Handles:

Appointment cancellation

Confirmation before deletion

Rescheduling Agent

Handles:

Moving appointments to new slots

Slot availability validation

⚙️ Technology Stack
Component	Technology
Agent Framework	LangGraph
LLM	Groq (Llama-3.3-70B)
AI Toolkit	LangChain
Data Storage	CSV
UI	Streamlit / CLI
Data Processing	Pandas
Validation	Pydantic
📂 Project Structure
Dental-Doctor-Appointment-System--Agentic-AI
│
├── main.py
├── streamlit_app.py
├── doctor_availability.csv
├── requirements.txt
│
├── dental_agent
│
│   ├── agent.py
│
│   ├── config
│   │   └── settings.py
│
│   ├── models
│   │   └── state.py
│
│   ├── tools
│   │   ├── csv_reader.py
│   │   └── csv_writer.py
│
│   ├── agents
│   │   ├── supervisor.py
│   │   ├── info_agent.py
│   │   ├── booking_agent.py
│   │   ├── cancellation_agent.py
│   │   └── rescheduling_agent.py
│
│   └── workflows
│       └── graph.py
🛠 Installation
1️⃣ Clone the repository
git clone https://github.com/MedisettiVinay0519/Dental-Doctor-Appointment-System--Agentic-AI.git
cd Dental-Doctor-Appointment-System--Agentic-AI
2️⃣ Create virtual environment
python -m venv venv

Activate it

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add API key

Create .env

GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0
▶️ Run the System
CLI Interface
python main.py
Streamlit Chat UI
streamlit run streamlit_app.py
💬 Example Queries
Check slots
Show available slots for orthodontist
Book appointment
Book patient 1000082 with Kevin Anderson on 02/09/2026 09:00
Cancel appointment
Cancel appointment for patient 1000082 at 02/09/2026 09:00
Reschedule
Reschedule patient 1000082 from 02/09/2026 09:00 to 03/09/2026 10:00
🦷 Available Specializations

General Dentist

Oral Surgeon

Orthodontist

Cosmetic Dentist

Prosthodontist

Pediatric Dentist

Emergency Dentist

📊 Data Model

Appointments are stored in doctor_availability.csv

Column	Description
date_slot	Appointment date and time
specialization	Dentist specialization
doctor_name	Dentist name
is_available	Slot availability
patient_to_attend	Patient ID
🎓 Educational Value

This project demonstrates important AI Engineering concepts:

Agent Orchestration

LangGraph manages the multi-agent workflow.

Tool-Augmented LLMs

Agents interact with tools to read and modify appointment data.

State Management

Conversation context and task parameters are preserved across agents.

Intent-Based Routing

User requests are dynamically routed based on detected intent.

📈 Future Improvements

Web UI using React

Database integration (PostgreSQL)

Deployment using Docker

Real-time notifications

Multi-clinic support

📜 License

This project is for educational and research purposes.

✅ This version is much stronger for GitHub and recruiters.

If you want, I can also show you 3 small changes that make this project look like a serious AI engineering project (used by startups).

i used streamlot and fastapi

Got it 👍 Since your project uses LangGraph + Groq + CSV + FastAPI + Streamlit, your README should reflect both interfaces (API backend + Streamlit UI). I’ll give you a clean final README version tailored to that stack.

🦷 Dental Doctor Appointment System — Agentic AI

A multi-agent AI system for managing dental appointments using LangGraph, Groq LLM, FastAPI, and Streamlit.

The system allows users to interact with a conversational AI assistant to:

Check available appointment slots

Book dental appointments

Cancel appointments

Reschedule appointments

This project demonstrates Agentic AI architecture, where specialized agents collaborate under a Supervisor Agent to complete tasks.

🚀 Features

🗓️ View available appointment slots

👨‍⚕️ Find doctors by specialization

📅 Book appointments via natural language

❌ Cancel existing bookings

🔄 Reschedule appointments

🤖 Multi-agent orchestration with LangGraph

🌐 FastAPI backend for AI agent execution

💬 Streamlit chat interface for user interaction

📊 CSV-based storage (lightweight database)

🧠 Architecture

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
⚙️ Technology Stack
Component	Technology
Agent Framework	LangGraph
LLM	Groq (Llama 3.3 70B)
AI Toolkit	LangChain
Backend API	FastAPI
Frontend UI	Streamlit
Data Storage	CSV
Data Processing	Pandas
Validation	Pydantic
📂 Project Structure
Dental-Doctor-Appointment-System--Agentic-AI
│
├── main.py
├── streamlit_app.py
├── api.py
├── doctor_availability.csv
├── requirements.txt
│
├── dental_agent
│
│   ├── agent.py
│
│   ├── config
│   │   └── settings.py
│
│   ├── models
│   │   └── state.py
│
│   ├── tools
│   │   ├── csv_reader.py
│   │   └── csv_writer.py
│
│   ├── agents
│   │   ├── supervisor.py
│   │   ├── info_agent.py
│   │   ├── booking_agent.py
│   │   ├── cancellation_agent.py
│   │   └── rescheduling_agent.py
│
│   └── workflows
│       └── graph.py
🛠 Installation
1️⃣ Clone the repository
git clone https://github.com/MedisettiVinay0519/Dental-Doctor-Appointment-System--Agentic-AI.git
cd Dental-Doctor-Appointment-System--Agentic-AI
2️⃣ Create virtual environment
python -m venv venv

Activate it

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure environment variables

Create .env

GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0
▶️ Running the System
Option 1 — CLI Mode
python main.py
Option 2 — Run FastAPI Backend
uvicorn api:app --reload

API documentation:

http://127.0.0.1:8000/docs
Option 3 — Run Streamlit UI
streamlit run streamlit_app.py

Streamlit UI:

http://localhost:8501
💬 Example Queries
View available slots
Show available slots for orthodontist
Book appointment
Book patient 1000082 with Kevin Anderson on 02/09/2026 09:00
Cancel appointment
Cancel appointment for patient 1000082 at 02/09/2026 09:00
Reschedule appointment
Reschedule patient 1000082 from 02/09/2026 09:00 to 03/09/2026 10:00
📊 Data Model

Appointment data is stored in doctor_availability.csv

Field	Description
date_slot	Appointment date and time
specialization	Dentist specialization
doctor_name	Dentist name
is_available	Slot availability
patient_to_attend	Patient ID
🎓 Learning Concepts

This project demonstrates:

Agentic AI systems

LangGraph multi-agent orchestration

LLM tool calling

Supervisor-agent architecture

FastAPI backend integration

Streamlit AI interfaces

📈 Future Improvements

React frontend

PostgreSQL database

Docker deployment

Multi-clinic scheduling

Real-time notifications

📜 License

This project is intended for educational and research purposes.

✅ This version makes your project look like a serious AI engineering project.

If you want, I can also help you add 3 things that will massively boost this repo on GitHub (stars + recruiter attention).
