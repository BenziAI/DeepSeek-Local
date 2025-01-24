import requests
import json
from typing import Dict, Optional

class DeepSeekClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url

    def generate(self, 
                prompt: str, 
                model: str = "deepseek-r1:1.5b",
                stream: bool = False,
                options: Optional[Dict] = None) -> str:
        """
        Generate a response from the DeepSeek model.
        
        Args:
            prompt (str): The input prompt for the model
            model (str): The model to use (default: deepseek-r1:1.5b)
            stream (bool): Whether to stream the response
            options (dict): Additional options for the model
        
        Returns:
            str: The generated response
        """
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream,
            "system": "You are a helpful AI assistant."
        }
        if options:
            payload.update(options)

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            print(f"Error details: {str(e)}")
            return f"Error: {str(e)}"

def main():
    # Initialize the client
    client = DeepSeekClient()
    
    # Example prompts to test the model
    prompts = [
        "Explain what is Python in one sentence.",
        "Write a simple hello world function in Python.",
        "What are the key features of machine learning?",
        "How would you implement a basic web server?",
        "Explain the concept of object-oriented programming."
    ]
    
    print("Testing DeepSeek API with different prompts:\n")
    for prompt in prompts:
        print(f"Prompt: {prompt}")
        response = client.generate(prompt)
        print(f"Response: {response}\n")
        print("-" * 80 + "\n")

if __name__ == "__main__":
    main() 