# app/main.py

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Prompt Firewall",
    description="Detects and blocks AI jailbreak & prompt injection attacks",
    version="1.0"
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
