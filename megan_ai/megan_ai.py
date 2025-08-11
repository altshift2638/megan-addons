from fastapi import FastAPI, Request
import openai
import os

# API Key baked in (yours)
openai.api_key = ""

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    if not user_message:
        return {"error": "No message provided"}

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are Megan, a friendly, casual AI assistant."},
                  {"role": "user", "content": user_message}]
    )

    reply = completion.choices[0].message["content"]
    return {"reply": reply}
