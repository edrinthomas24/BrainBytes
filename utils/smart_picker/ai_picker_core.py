from .gpt4 import get_gpt4_response
from .gemini import get_gemini_response
from .claude import get_claude_response
from .deepseek import get_deepseek_response
from .embedder import get_embedding
from .compare import compare_embeddings

def smart_ai(prompt):
    results = {}
    prompt_emb = get_embedding(prompt)

    try:
        gpt_resp = get_gpt4_response(prompt)
        results['GPT-4'] = (gpt_resp, compare_embeddings(prompt_emb, get_embedding(gpt_resp)))
    except: results['GPT-4'] = ("Error", 0)

    try:
        gemini_resp = get_gemini_response(prompt)
        results['Gemini'] = (gemini_resp, compare_embeddings(prompt_emb, get_embedding(gemini_resp)))
    except: results['Gemini'] = ("Error", 0)

    try:
        claude_resp = get_claude_response(prompt)
        results['Claude'] = (claude_resp, compare_embeddings(prompt_emb, get_embedding(claude_resp)))
    except: results['Claude'] = ("Error", 0)

    try:
        deepseek_resp = get_deepseek_response(prompt)
        results['DeepSeek'] = (deepseek_resp, compare_embeddings(prompt_emb, get_embedding(deepseek_resp)))
    except: results['DeepSeek'] = ("Error", 0)

    best_model = max(results.items(), key=lambda x: x[1][1])
    return f"**{best_model[0]}**
\n\n{best_model[1][0]}"
