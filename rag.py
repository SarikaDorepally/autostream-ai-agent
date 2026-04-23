import json

def load_knowledge():
    with open("data/knowledge.json", "r") as f:
        return json.load(f)

def retrieve_answer(query):
    data = load_knowledge()
    query = query.lower()

    if any(word in query for word in ["price", "pricing", "plan", "plans"]):
        return f"Basic Plan: {data['plans']['Basic Plan']}\nPro Plan: {data['plans']['Pro Plan']}"

    elif any(word in query for word in ["refund", "policy", "support"]):
        return f"Refund Policy: {data['policies']['refund']}\nSupport: {data['policies']['support']}"

    return "I can help with pricing, plans, and policies!"
