# DeepSeek Local Client

A Python client for running the DeepSeek LLM locally using Ollama. This client provides a simple interface to interact with the DeepSeek model through Ollama's API.

## Features

- Simple Python interface for DeepSeek model interactions
- Support for both single prompts and batch processing
- Configurable model parameters
- Error handling and detailed logging

## Prerequisites

1. Install Ollama from [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
2. Python 3.7 or higher
3. Required Python packages (install using `pip install -r requirements.txt`)

## Setup

1. Install Ollama and verify it's running:
```bash
ollama --version
```

2. Pull the DeepSeek model:
```bash
ollama pull deepseek-r1:1.5b
```

3. Start the Ollama server:
```bash
ollama serve
```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script to test various prompts:
```bash
python deepseek_client.py
```

### Using in Your Own Code

You can import and use the DeepSeekClient in your own Python code:

```python
from deepseek_client import DeepSeekClient

client = DeepSeekClient()
response = client.generate(
    prompt="Your prompt here",
    model="deepseek-r1:1.5b",  # or any other model you've pulled
    options={
        "temperature": 0.7,
        "max_tokens": 100
    }
)
print(response)
```

## Model Information

The DeepSeek R1 Distill Qwen 1.5B model specifications:
- Architecture: Qwen2
- Size: 1.5B parameters
- Format: GGUF V3
- Quantization: Q4_K - Medium
- Model Size: 1.04 GiB
- Context Length: 8192 tokens

## GitHub Integration

If you're using this with Git:

1. Clone the repository:
```bash
git clone <your-repo-url>
cd DeepSeek
```

2. Make changes and commit:
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

## Troubleshooting

1. If you get a 404 error, make sure:
   - Ollama server is running (`ollama serve`)
   - DeepSeek model is pulled (`ollama pull deepseek-r1:1.5b`)
   - You're using the correct model name

2. If the server isn't responding:
   - Check if Ollama is running
   - Verify the port (11434) is not blocked
   - Restart the Ollama server if needed

## License

This project is open source and available under the MIT License. 