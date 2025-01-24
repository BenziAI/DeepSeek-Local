# DeepSeek Local Client

A professional Python client for running the DeepSeek LLM locally using Ollama. This client provides a clean, simple interface to interact with DeepSeek's powerful language model through Ollama's API.

![DeepSeek](https://raw.githubusercontent.com/BenziAI/DeepSeek-Local/main/assets/banner.png)

## Features

- 🚀 Simple Python interface for DeepSeek model interactions
- 🔄 Support for both single prompts and batch processing
- ⚙️ Configurable model parameters and settings
- 🛡️ Built-in error handling and logging
- 📝 Comprehensive documentation and examples

## Model Specifications

The DeepSeek R1 Distill Qwen 1.5B model specifications:
- Architecture: Qwen2
- Size: 1.5B parameters
- Format: GGUF V3
- Quantization: Q4_K - Medium
- Model Size: 1.04 GiB
- Context Length: 8192 tokens
- Memory Usage: ~2GB RAM

## Prerequisites

1. Install Ollama from [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
2. Python 3.7 or higher
3. Required Python packages (install using `pip install -r requirements.txt`)

## Quick Start

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

### Basic Usage
Run the example script to test various prompts:
```bash
python deepseek_client.py
```

### Integration in Your Code
You can import and use the DeepSeekClient in your own Python code:

```python
from deepseek_client import DeepSeekClient

client = DeepSeekClient()
response = client.generate(
    prompt="Your prompt here",
    model="deepseek-r1:1.5b",
    options={
        "temperature": 0.7,
        "max_tokens": 100
    }
)
print(response)
```

## Advanced Configuration

The client supports various configuration options:

```python
options = {
    "temperature": 0.7,      # Controls randomness (0.0 to 1.0)
    "max_tokens": 100,       # Maximum length of response
    "top_p": 0.9,           # Nucleus sampling parameter
    "top_k": 40,            # Top-k sampling parameter
    "system": "Custom system prompt"  # System prompt for context
}
```

## Troubleshooting

1. If you get a 404 error:
   - Ensure Ollama server is running (`ollama serve`)
   - Verify DeepSeek model is pulled (`ollama pull deepseek-r1:1.5b`)
   - Check model name matches exactly

2. If the server isn't responding:
   - Check if Ollama is running
   - Verify port 11434 is not blocked
   - Restart the Ollama server if needed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Thanks to the [Ollama](https://github.com/ollama/ollama) team for their amazing work
- Thanks to [DeepSeek](https://github.com/deepseek-ai) for the model architecture

## Support

If you encounter any issues or have questions, please:
1. Check the [Troubleshooting](#troubleshooting) section
2. Open an issue on GitHub
3. Join our community discussions 