from .gemini import get_gemini_response
from .llama import get_llama_response
from .deepseek import get_deepseek_response
from .cohere import get_cohere_response
from .embedder import get_embedding
from .compare import compare_embeddings

def smart_ai(prompt):
    results = {}
    prompt_emb = get_embedding(prompt)

    try:
        gemini_resp = get_gemini_response(prompt)
        results['Gemini'] = (gemini_resp, compare_embeddings(prompt_emb, get_embedding(gemini_resp)))
    except: results['Gemini'] = ("Error", 0)

    try:
        llama_resp = get_llama_response(prompt)
        results['LLaMA'] = (llama_resp, compare_embeddings(prompt_emb, get_embedding(llama_resp)))
    except: results['LLaMA'] = ("Error", 0)

    try:
        deepseek_resp = get_deepseek_response(prompt)
        results['DeepSeek'] = (deepseek_resp, compare_embeddings(prompt_emb, get_embedding(deepseek_resp)))
    except: results['DeepSeek'] = ("Error", 0)

    try:
        cohere_resp = get_cohere_response(prompt)
        results['Cohere'] = (cohere_resp, compare_embeddings(prompt_emb, get_embedding(cohere_resp)))
    except: results['Cohere'] = ("Error", 0)

    best_model = max(results.items(), key=lambda x: x[1][1])
    return f"**{best_model[0]}**\n\n{best_model[1][0]}"
