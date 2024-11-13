from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Get API key and base URL from environment variables
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

# Initialize the OpenAI client with NVIDIA API details
client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

# Define the request model
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(request: PromptRequest):
    try:
        # Asynchronously send the prompt to the NVIDIA model
        completion = await asyncio.to_thread(
            client.chat.completions.create,
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": request.prompt}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )
        
        # Collect the response in chunks and concatenate it
        response_text = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response_text += chunk.choices[0].delta.content

        return {"response": response_text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
