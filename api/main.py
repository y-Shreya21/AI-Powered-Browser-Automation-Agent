# api/main.py

from fastapi import FastAPI

app = FastAPI(title="AI Browser Agent")

@app.get("/")
async def root():
    return {"status": "running"}