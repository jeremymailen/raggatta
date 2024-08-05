import os
from typing import Optional
from langchain_anthropic import ChatAnthropic

api_key = os.environ.get("ANTHROPIC_API_KEY")
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", api_key=api_key)
prompt_template = """Answer the question based on the following context:
{context}
Question: {question}
"""


def ask_claude(question: str, context: Optional[str] = None) -> str:
    prompt = prompt_template.format(question=question, context=context or "No context provided")
    response = llm.invoke(prompt)
    return response.content
