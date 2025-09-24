# AI Chatbox

A full-stack AI chatbot application demonstrating end-to-end integration of frontend, backend, and model services. Users can interact with a language model through a web interface, while the backend handles API calls and optional caching.

---

## Project Structure

ai-chatbox/
│
├── frontend/ # ReactJS frontend for chat interface
├── backend/ # FastAPI backend service
├── model-svc/ # AI model service (Hugging Face / local / API models)
├── docker-compose.yml # Orchestrates frontend, backend, and model services
└── README.md


---

## Tech Stack

- **Frontend:** ReactJS  
- **Backend:** FastAPI, Python, HTTPX  
- **Model Service:** Hugging Face Transformers (distilgpt2 currently), can be replaced with OpenAI / Anthropic API or local LLM  
- **Caching / Queues:** Redis (optional)  
- **Containerization:** Docker, Docker Compose  

---

## Features Implemented

1. **Frontend**
   - Chat UI built in ReactJS  
   - Sends user prompts to backend API  
   - Handles responses and displays them  

2. **Backend**
   - FastAPI backend service exposes `/chat` endpoint  
   - Calls model service (`model-svc`) to generate responses  
   - Handles CORS to allow frontend requests  
   - Added configurable timeout to avoid `httpx.ReadTimeout`  

3. **Model Service**
   - Currently running Hugging Face **distilgpt2**  
   - Receives text prompts and generates responses  
   - Can be extended to:  
     - Local LLM (LLaMA, Mistral, GPT4All, etc.)  
     - OpenAI / Anthropic API calls  
   - Response is returned to backend → frontend  

4. **Docker Integration**
   - `docker-compose` sets up backend, frontend, model service, and Redis  
   - Allows seamless end-to-end local development  

---

## Next Steps (Planned)

- **Improve model layer:**  
  - Plug in high-quality local LLMs or OpenAI / Anthropic APIs  
  - Experiment with hybrid setup for cost and performance optimization  

- **Frontend Enhancements:**  
  - Stream responses  
  - Chat history storage  
  - Markdown rendering  

- **Backend Enhancements:**  
  - Add user authentication (optional)  
  - Add Redis caching for conversation context  
  - Support multiple model endpoints  

---

## How to Run Locally

```bash
# Clone repo
git clone <repo-url>
cd ai-chatbox

# Start all services
docker-compose up --build
