from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class RequestBody(BaseModel):
    prompt: str
    max_length: int = 100

generator = pipeline("text-generation", model="distilgpt2")

@app.post("/generate")
async def generate(req: RequestBody):
    out = generator(req.prompt, max_length=req.max_length, num_return_sequences=1)
    return {"text": out[0]["generated_text"]}

