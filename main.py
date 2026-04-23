from agent import handle_conversation
from memory import AgentState

def run():
    print("🤖 AutoStream AI Agent Started! Type 'exit' to quit.\n")
    state = AgentState()

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        response = handle_conversation(user_input, state)
        print("Bot:", response)

if __name__ == "__main__":
    run()
