import asyncio
import websockets
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

async def chatbot(websocket, path):
    async for message in websocket:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}]
        )
        await websocket.send(response["choices"][0]["message"]["content"])

start_server = websockets.serve(chatbot, "localhost", 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
