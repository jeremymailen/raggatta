import os
from langchain_anthropic import ChatAnthropic

api_key = os.environ.get("ANTHROPIC_API_KEY")
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", api_key=api_key)


def ask_claude(prompt: str) -> str:
    messages = [
        ("system", "You are answering general questions."),
        ("human", prompt),
    ]
    response = llm.invoke(messages)
    return response.content
