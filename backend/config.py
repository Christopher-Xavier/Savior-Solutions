import json

def get_api_key():
    with open("config.json") as f:
        config = json.load(f)
    return config["OPENAI_API_KEY"]
