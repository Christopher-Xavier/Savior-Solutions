import os
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from dotenv import load_dotenv
import os
from config import get_api_key

api_key = get_api_key()  # Loads key securely


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = "YOUR_OPENAI_API_KEY"

api_key = os.getenv("OPENAI_API_KEY")

def get_tech_advice(user_query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_query}]
    )
    return response["choices"][0]["message"]["content"]

query = "Why is my laptop overheating?"
print(get_tech_advice(query))

app = Flask(__name__)
CORS(app)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return jsonify({"reply": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
import asyncio
import websockets

async def chatbot(websocket, path):
    async for message in websocket:
        response = f"TechBot: Based on your issue, I suggest checking network settings."
        await websocket.send(response)

start_server = websockets.serve(chatbot, "localhost", 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
