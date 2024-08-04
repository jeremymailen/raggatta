import sys
from app import prompt

if (len(sys.argv) < 2):
    print("Usage: python -m app <prompt>")
    print("Example: python -m app 'What is your name?'")
    sys.exit(1)

response = prompt.ask_claude(sys.argv[1])
print(f"Response: {response}")
