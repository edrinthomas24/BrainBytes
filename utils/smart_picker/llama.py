def get_llama_response(prompt):
    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-2-70b-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://api.llama-api.com/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"].strip()
