import requests

def get_groq_response(prompt):
    url = "https://api.groq.com/chat/completions"
    headers = {
        "Authorization": "Bearer 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"
    }
    data = {
        "messages": [
            {"role": "system", "content": "you are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "model": "llama3-8b-8192"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()
