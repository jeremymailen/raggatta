# raggatta

An LLM rag demo

## Setup

Install https://brew.sh

Tools:

```shell
brew install python poetry
```

Dependencies:

```shell
poetry install --no-root
````

API Keys for Claude and Langchain:

```shell
export ANTHROPIC_API_KEY=your-claude-api-key
exec LANGCHAIN_API_KEY=your-langchain-api-key
```

## Run

```shell
poetry run python -m app 'Who is Nelson Mandela?'
```
