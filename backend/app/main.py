from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.knowledge_base import SYMPTOMS_DB
from app.engine import ChainingEngine

app = FastAPI(title="Rule-Based Diagnosis System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ForwardRequest(BaseModel):
    symptoms: list[str]

class BackwardRequest(BaseModel):
    rule_id: str
    all_symptoms: list[str]

@app.get("/api/symptoms")
def get_symptoms():
    return SYMPTOMS_DB

@app.post("/api/forward-chain")
def run_forward_chain(req: ForwardRequest):
    return {"candidates": ChainingEngine.forward_chain(req.symptoms)}

@app.post("/api/backward-chain")
def run_backward_chain(req: BackwardRequest):
    return {"result": ChainingEngine.backward_chain(req.rule_id, req.all_symptoms)}