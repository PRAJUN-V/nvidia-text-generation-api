# NVIDIA Text Generation API

This project is a FastAPI-based application that integrates with the NVIDIA text generation model to generate text responses from user-provided prompts. It uses the `OpenAI` client to interact with NVIDIA's API, making it easy to deploy and scale for various applications.

## Features
- Accepts POST requests with a user-provided prompt.
- Returns AI-generated text based on the NVIDIA model.
- Utilizes environment variables for sensitive configuration data.

## Requirements
- Python 3.7+
- NVIDIA API Key and Base URL

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/PRAJUN-V/nvidia-text-generation-api.git
cd nvidia-text-generation-api

Create a .env File,
Add your NVIDIA API key and base URL to a .env file in the root directory of the project:
API_KEY=your_nvidia_api_key
BASE_URL=https://integrate.api.nvidia.com/v1

Install Dependencies
```markdown
pip install fastapi pydantic openai python-dotenv
```

Run the Application
```markdown
uvicorn main:app --reload
```