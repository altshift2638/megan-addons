import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.5"))

if not OPENAI_API_KEY:
    raise RuntimeError("Set OPENAI_API_KEY in add-on options (Add-ons -> Megan AI (ChatGPT) -> Configuration)")

client = OpenAI(api_key=OPENAI_API_KEY)
app = FastAPI(title="Megan AI (ChatGPT)", version="1.0.0")

SYSTEM_PROMPT = (
    "You are Megan, a warm, casual home assistant integrated with Home Assistant. "
    "Be concise, friendly, and helpful. If the user asks about devices, answer plainly."
)

@app.get("/health")
def health():
    return {"status": "ok", "provider": "openai", "model": OPENAI_MODEL}

@app.post("/chat")
def chat(payload: dict):
    text = (payload.get("message") or "").strip()
    if not text:
        raise HTTPException(400, "Missing 'message'")
    r = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=TEMPERATURE,
    )
    reply = r.choices[0].message.content
    return {"reply": reply}

@app.get("/demo")
def demo():
    return HTMLResponse("""
<!doctype html><meta charset="utf-8">
<title>Megan — ChatGPT</title>
<style>body{font-family:system-ui;padding:20px;max-width:760px;margin:auto}</style>
<h2>Megan (ChatGPT)</h2>
<textarea id=t rows=5 style="width:100%" placeholder="Ask Megan…"></textarea><br>
<button onclick="send()">Ask</button>
<pre id=o></pre>
<script>
async function send(){
  const txt=document.getElementById('t').value.trim();
  o.textContent="Thinking…";
  const r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:txt})});
  const j=await r.json(); o.textContent=j.reply||JSON.stringify(j,null,2);
}
const o=document.getElementById('o');
</script>
""")
