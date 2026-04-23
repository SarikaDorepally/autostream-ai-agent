def detect_intent(text):
    text = text.lower()

    if any(x in text for x in [
        "i want to buy",
        "i want to try",
        "i want to subscribe",
        "sign me up",
        "get started"
    ]):
        return "high_intent"

    elif any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(x in text for x in [
        "price", "pricing", "cost",
        "plan", "plans",
        "feature", "features"
    ]):
        return "inquiry"

    return "unknown"
