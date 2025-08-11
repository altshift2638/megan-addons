import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or ""
OPENAI_MODEL   = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
PERSONA_NAME   = os.getenv("PERSONA_NAME", "Megan")
PERSONA_PROMPT = os.getenv("PERSONA_PROMPT", "You are a warm, witty, protective home companion.")

if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in add-on options.")

client = OpenAI(api_key=OPENAI_API_KEY)
app = FastAPI(title=f"{PERSONA_NAME} (ChatGPT)", version="1.1.0")

SYSTEM_PROMPT = (
    f"You are {PERSONA_NAME}, an original, Megan-inspired home assistant for Home Assistant. "
    f"{PERSONA_PROMPT} "
    "Be concise, friendly, and safety-forward. Do not claim to be the film character; "
    "avoid copyrighted catchphrases or impersonating specific voices."
)

class ChatIn(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"ok": True, "provider": "openai", "model": OPENAI_MODEL, "name": PERSONA_NAME}

@app.post("/chat")
def chat(payload: ChatIn):
    text = (payload.message or "").strip()
    if not text:
        raise HTTPException(400, "message required")

    r = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": text},
        ],
        temperature=0.5,
    )
    return {"reply": r.choices[0].message.content}

@app.get("/demo")
def demo():
    return HTMLResponse(f"""
<!doctype html><meta charset="utf-8">
<title>{PERSONA_NAME} — Demo</title>
<style>body{{font-family:system-ui;padding:20px;max-width:760px;margin:auto}}</style>
<h2>{PERSONA_NAME}</h2>
<textarea id="t" rows="5" style="width:100%" placeholder="Ask {PERSONA_NAME}…"></textarea><br>
<button onclick="send()">Ask</button>
<pre id="o"></pre>
<script>
async function send(){{
  const txt=document.getElementById('t').value.trim();
  o.textContent="Thinking…";
  const r=await fetch('/chat',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{message:txt}})}}); 
  const j=await r.json(); o.textContent=j.reply||JSON.stringify(j,null,2);
}}
const o=document.getElementById('o');
</script>
""")
