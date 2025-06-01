import json

with open("config.json") as f:
    config = json.load(f)

api_key = config["OPENAI_API_KEY"]
print(api_key)  # Verifies retrieval
