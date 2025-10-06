from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
from redis import asyncio as aioredis
from ctransformers import AutoModelForCausalLM

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# MODEL_URL = "http://model-svc:8001/generate"
redis=None

model = AutoModelForCausalLM.from_pretrained(
    "./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    model_file="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    model_type="llama"
)

class RequestBody(BaseModel):
    prompt: str

@app.on_event("startup")
async def startup_event():
    global redis
    redis = await aioredis.from_url("redis://redis:6379")

@app.post("/chat")
async def chat(req: RequestBody):
    # cache_key = f"resp:{req.prompt}"
    # cached = await redis.get(cache_key)
    # if cached:
    #     return {"text": cached.decode(), "source": "cache"}
    
    # async with httpx.AsyncClient(timeout=60.0) as client:
    #     resp = await client.post(MODEL_URL, json={"prompt": req.prompt})
    #     try:
    #         data = resp.json()
    #     except:
    #         data = {"raw": resp.text}
    #     await redis.set(cache_key, data["text"], ex=3600)
    #     return {"text": data["text"], "source": "model"}
    prompt = req.prompt.strip()
    if not prompt:
        return {"response": "Enter a valid prompt"}
    response = model(prompt, max_new_tokens=200)
    return {"response": response}