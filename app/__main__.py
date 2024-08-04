import sys
from app import chat

if (len(sys.argv) < 2):
    print("Usage: python -m app <prompt>")
    print("Example: python -m app 'What is your name?'")
    sys.exit(1)

response = chat.ask_claude(sys.argv[1])
print(f"Response: {response}")
