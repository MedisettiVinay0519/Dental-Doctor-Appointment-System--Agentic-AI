from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from dental_agent.agent import dental_graph

app = FastAPI(
    title="Dental Appointment AI",
    description="FastAPI backend for LangGraph Dental Appointment System",
    version="1.0"
)

# Request schema
class ChatRequest(BaseModel):
    message: str


# Response schema
class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {"message": "Dental Appointment AI API is running"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = dental_graph.invoke({
        "messages": [HumanMessage(content=request.message)]
    })

    final_message = result["messages"][-1].content

    return {"response": final_message}
