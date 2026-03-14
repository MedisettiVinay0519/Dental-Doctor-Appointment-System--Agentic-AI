# 🦷 Dental Doctor Appointment System — Agentic AI

A **multi-agent AI system for managing dental appointments** using **LangGraph and Groq LLM**.

The system allows users to interact with a conversational AI assistant to:

- Check available appointment slots
- Book dental appointments
- Cancel appointments
- Reschedule appointments

This project demonstrates **Agentic AI architecture**, where specialized agents collaborate under a **Supervisor Agent** to complete tasks.

---

# 🚀 Features

- 🗓️ View available appointment slots  
- 👨‍⚕️ Find doctors by specialization  
- 📅 Book appointments via natural language  
- ❌ Cancel existing bookings  
- 🔄 Reschedule appointments  
- 🤖 Multi-agent orchestration with LangGraph  
- 📊 CSV-based storage (lightweight database)

---

# 🧠 Architecture

The system follows a **Supervisor-Agent architecture**.

```
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

---

# ⚙️ Technology Stack

| Component | Technology |
|--------|--------|
| Agent Framework | LangGraph |
| LLM | Groq (Llama 3.3 70B) |
| AI Toolkit | LangChain |
| Data Storage | CSV |
| Data Processing | Pandas |
| Validation | Pydantic |

---

# 📂 Project Structure

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

---

# 🛠 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MedisettiVinay0519/Dental-Doctor-Appointment-System--Agentic-AI.git
cd Dental-Doctor-Appointment-System--Agentic-AI
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure environment variables

Create `.env`

```
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0
```

---

# ▶️ Running the System

Run the CLI application:

```bash
python main.py
```

---

# 💬 Example Queries

### View available slots

```
Show available slots for orthodontist
```

### Book appointment

```
Book patient 1000082 with Kevin Anderson on 02/09/2026 09:00
```

### Cancel appointment

```
Cancel appointment for patient 1000082 at 02/09/2026 09:00
```

### Reschedule appointment

```
Reschedule patient 1000082 from 02/09/2026 09:00 to 03/09/2026 10:00
```

---

# 📊 Data Model

Appointment data is stored in **doctor_availability.csv**

| Field | Description |
|------|-------------|
| date_slot | Appointment date and time |
| specialization | Dentist specialization |
| doctor_name | Dentist name |
| is_available | Slot availability |
| patient_to_attend | Patient ID |

---

# 🎓 Learning Concepts

This project demonstrates:

- **Agentic AI systems**
- **LangGraph multi-agent orchestration**
- **LLM tool calling**
- **Supervisor-agent architecture**

---

# 📈 Future Improvements

- Web UI integration
- PostgreSQL database
- Docker deployment
- Multi-clinic scheduling
- Real-time notifications

---

# 📜 License

This project is intended for **educational and research purposes**.
