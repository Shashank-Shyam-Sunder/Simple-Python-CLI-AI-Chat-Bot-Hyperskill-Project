# Simple Python CLI Chat

A minimal, ready-to-run command‑line chatbot powered by the OpenAI Chat Completions API. This project contains one main script:
- **File Location:** `Simple Python CLI Chat\task\simple_cli_AI_chatbot.py` — Interactive multi‑turn chatbot with function calling capability and token cost reporting.

The script uses the OpenAI Python SDK, loads your API key from a local .env file, and by default connects to a proxy base URL provided for the course environment (but can be configured to use OpenAI directly).

**⚠️ Important Note:** If you use the code with the `base_url` parameter, you need a unique API key that works specifically with that base URL. For local testing and running the chatbot, it is recommended to skip the `base_url` and use a standard OpenAI API key instead.


## Features
- Loads OPENAI_API_KEY from a .env file using python‑dotenv.
- Uses OpenAI Chat Completions with model gpt-4o-mini.
- Interactive loop (simple_cli_AI_chatbot.py) for continuous chatting.
- Demonstrates tool (function calling) schema with an example end_conversation function.
- Prints an estimated token cost per request (based on sample pricing constants in the script).


## Prerequisites
- Python 3.9+ recommended
- An OpenAI‑compatible API key available in your environment (OPENAI_API_KEY)
- Access to the configured base URL (defaults in this project to a course proxy):
  https://litellm.aks-hs-prod.int.hyperskill.org/


## Installation
1) Create and activate a virtual environment (recommended).
   - Windows (PowerShell):
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1

2) Install dependencies from requirements_project.txt:
   pip install -r requirements_project.txt

Note: requirements.txt is intentionally ignored in this repository; use requirements_project.txt instead.


## Environment setup
Create a .env file at the project root (or where you run the script) with:
OPENAI_API_KEY=your_api_key_here

The script calls load_dotenv() to read this variable.


## Usage
To run the chatbot, execute the following command (ensure OPENAI_API_KEY is set):

python "Simple Python CLI Chat\Simple Python CLI Chat\task\simple_cli_AI_chatbot.py"

What it does:
- Prompts you for input in a continuous interactive loop.
- Sends your message to the model gpt-4o-mini using the configured base URL.
- Prints the assistant response.
- Shows an estimated cost using this pricing table in USD per 1K tokens: input $0.01, output $0.03.
- Includes a tool schema for a function named end_conversation. When the model triggers a tool call, the script prints details and exits the loop.

Tip: You can type "End Conversation" to hint the assistant to end the dialogue; the sample function schema advertises this capability. Whether it's invoked depends on the model/tool behavior.


## Configuration
- Model: gpt-4o-mini
- Temperature: 0.8
- Base URL: https://litellm.aks-hs-prod.int.hyperskill.org/ (course proxy)
- Token cost estimation:
  - Input: $0.01 per 1,000 tokens
  - Output: $0.03 per 1,000 tokens
  These are example constants used to estimate cost via the usage fields in the API response. Adjust values as needed.

**Using OpenAI directly:** If you want to use the public OpenAI API instead of the course proxy, simply remove the `base_url` parameter from the client initialization in the script. This allows you to access official OpenAI models directly with just your API key.


## Troubleshooting
- Missing API key: The script raises KeyError("Missing API Key. Check your .env file.") when OPENAI_API_KEY is not set or visible. Ensure .env is in the working directory and contains the key, or set the environment variable directly.
- Path on Windows: If running from an IDE or different working directory, ensure the relative path to .env is correct. The script includes commented examples for manually specifying the .env path.
- Network access: Ensure your environment can reach the configured base_url and that your key is valid for it.
- Dependencies: Make sure you installed from requirements_project.txt.


## Notes on repository tracking
- Only the file simple_cli_AI_chatbot.py is tracked inside the task directory; other Python files in that directory are ignored by .gitignore as part of the course scaffolding.
- requirements.txt is intentionally ignored; requirements_project.txt is the source of truth for dependencies.


## Using the public OpenAI API directly (no base_url)
If you want to use the official OpenAI API instead of the course proxy, you can easily modify the script by removing the `base_url` parameter. This allows you to access OpenAI models directly, including future models like ChatGPT 5 when they become available.

**Quick modification:** In the `simple_cli_AI_chatbot.py` file, change line 56 from:
```python
client = openai.OpenAI(api_key=api_key, base_url="https://litellm.aks-hs-prod.int.hyperskill.org/")
```
to:
```python
client = openai.OpenAI(api_key=api_key)
```

**Complete example for direct OpenAI usage:**
```python
import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise KeyError("Missing API Key. Check your .env file.")

client = openai.OpenAI(api_key=api_key)  # No base_url needed

resp = client.chat.completions.create(
    model="gpt-4o-mini",  # or gpt-4o, gpt-4, etc.
    messages=[{"role": "user", "content": "Hello"}],
    temperature=0.8,
)
print(resp.choices[0].message.content)
```

**Benefits of using OpenAI directly:**
- Access to the latest OpenAI models as they're released
- Direct connection to OpenAI's servers (potentially better performance)
- Future access to models like ChatGPT 5 when available via the API
- No dependency on the course proxy infrastructure

**Requirements:**
- Valid OpenAI API key with sufficient credits
- Ensure your OPENAI_API_KEY is from your OpenAI account (not the course environment)
- Choose models available to your OpenAI subscription tier

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
