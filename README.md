# ChatBot LangChain with Groq

A modular and scalable chatbot implementation using FastAPI, LangChain, and Groq. This project provides a REST API for chat functionality with additional tools for text summarization and translation.

## Features

- 🤖 General chat functionality
- 📝 Text summarization
- 🌍 Text translation
- 🚀 FastAPI-based REST API
- 🐳 Docker support
- ⚡ Groq LLM integration

## Prerequisites

- Docker and Docker Compose
- Groq API Key

## Environment Setup

1. Clone the repository:
    ```bash
        git clone https://github.com/
    ```

2. Navigate to the project directory:
    ```bash
        cd chatbot-langchain
    ```

3. Copy the example environment file and update it with your credentials
    ```bash
        cp .env.example .env
    ```

4. Update the `.env` file with your Groq API key and other configurations:

## Running with Docker

1. Build the Docker image:
    ```bash
        docker build -t chatbot-langchain .
    ```

2. Run the Docker container:
    ```bash
        docker run -p 8080:8080 chatbot-langchain
    ```


The API will be available at `http://localhost:8080/api/v1`

## API Endpoints

### Health Check

- **Endpoint**: `/` 
- **Method**: `GET`
- **Response**: `{"health_check": "OK"}`

### Chat

- **Endpoint**: `/chat`
- **Method**: `POST`
- **Request Body**: `{"messages": [...], "tool": string, "text": string, "target_language": string}`
- **Response**: `{"response": string, "tool_used": string, "thoughts": string}`

Example with different tools:

Example with summarizer:

```json
{
    "tool": "summarizer",
    "text": "This is a sample text for summarization.",
}
```

Example with chat:
```json
{
    "messages": [
        {"role": "user", "content": "Hello!"}
    ],
    "tool": "chat"
}
```

Example with translator:

```json
{
    "tool": "translator",
    "text": "Hello, how are you?",
    "target_language": "spanish"
}
```


## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful request
- 400: Bad request (invalid input)
- 500: Server error

Error responses include a detail message explaining the error: