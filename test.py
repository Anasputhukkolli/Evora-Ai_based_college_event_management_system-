import requests

invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"

headers = {
    "Authorization": "Bearer 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",
    "Accept": "application/json",
}

payload = {
    "text_prompts": [
        {
            "text": "underwater world, plants, shells, creatures, high detail, sharp focus, 4k",
            "weight": 1
        },
        {
            "text":  "" ,
            "weight": -1
        }
    ],
    "cfg_scale": 5,
    "sampler": "K_DPM_2_ANCESTRAL",
    "seed": 0,
    "steps": 25
}

response = requests.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)