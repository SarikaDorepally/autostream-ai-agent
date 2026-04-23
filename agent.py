from intent import detect_intent
from rag import retrieve_answer
from tools import mock_lead_capture

def handle_conversation(user_input, state):

    if state.intent == "high_intent" and (
        state.name is None or state.email is None or state.platform is None
    ):
        return handle_lead_collection(user_input, state)

    intent = detect_intent(user_input)
    state.intent = intent

    if intent == "greeting":
        return "Hello! 👋 How can I help you with AutoStream?"

    elif intent == "inquiry":
        return retrieve_answer(user_input)

    elif intent == "high_intent":
        return "Awesome! Let's get you started. What's your name?"

    return "I can help with pricing, plans, or getting started!"

def handle_lead_collection(user_input, state):

    if state.name is None:
        state.name = user_input
        return "Great! Please provide your email."

    elif state.email is None:
        state.email = user_input
        return "Nice! Which platform do you create content on?"

    elif state.platform is None:
        state.platform = user_input
        mock_lead_capture(state.name, state.email, state.platform)

        state.name = None
        state.email = None
        state.platform = None
        state.intent = None

        return "🎉 You're all set! Our team will reach out soon."
