import argparse
from app import chat

args = argparse.ArgumentParser(
    prog="raggatta", description="Ask Claude a question with your data"
)
args.add_argument("-p", "--prompt", help="Prompt to ask Claude", required=True)
args.add_argument("-r", "--rag-data", help="RAG data to supplement the prompt")

params = args.parse_args()
print(params.prompt)

response = chat.ask_claude(params.prompt, "Johnny is on the Monorail. In a Song.")
print(f"Response: {response}")
