# Simple Python CLI Chat

A minimal, ready-to-run command‑line chatbot powered by the OpenAI Chat Completions API. This project includes two scripts:
- simple_cli_AI_chatbot.py — Interactive multi‑turn mode with a simple tool/function and token cost reporting.
- Simple Python CLI Chat/task/main.py — Single‑turn example that sends one prompt and prints the assistant’s reply and approximate cost.

The scripts use the OpenAI Python SDK, load your API key from a local .env file, and (in this template) talk to a proxy base URL provided for the course environment.


## Features
- Loads OPENAI_API_KEY from a .env file using python‑dotenv.
- Uses OpenAI Chat Completions with model gpt-4o-mini.
- Interactive loop (simple_cli_AI_chatbot.py) for continuous chatting.
- Demonstrates tool (function calling) schema with an example end_conversation function.
- Prints an estimated token cost per request (based on sample pricing constants in the scripts).


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

The scripts call load_dotenv() to read this variable.


## Usage
Project root directory layout (relevant parts):
- Simple Python CLI Chat/task/simple_cli_AI_chatbot.py
- Simple Python CLI Chat/task/main.py

You can run either script. Both require OPENAI_API_KEY to be set.

1) Interactive multi‑turn chat (recommended for demo):
   python "Simple Python CLI Chat\Simple Python CLI Chat\task\simple_cli_AI_chatbot.py"

   What it does:
   - Prompts you for input in a loop.
   - Sends your message to the model gpt-4o-mini using the configured base URL.
   - Prints the assistant response.
   - Shows an estimated cost using this pricing table in USD per 1K tokens: input $0.01, output $0.03.
   - Includes a tool schema for a function named end_conversation. When the model triggers a tool call, the script prints details and exits the loop.

   Tip: You can type End Conversation to hint the assistant to end the dialogue; the sample function schema advertises this capability. Whether it’s invoked depends on the model/tool behavior.

2) Single‑turn example (one prompt):
   python "Simple Python CLI Chat\Simple Python CLI Chat\task\main.py"

   What it does:
   - Asks for a single prompt via input().
   - Sends the prompt to the API and prints the response.
   - Prints the estimated cost for that single call.


## Configuration
- Model: gpt-4o-mini
- Temperature: 0.8 (both scripts)
- Base URL: https://litellm.aks-hs-prod.int.hyperskill.org/
- Token cost estimation:
  - Input: $0.01 per 1,000 tokens
  - Output: $0.03 per 1,000 tokens
  These are example constants used to estimate cost via the usage fields in the API response. Adjust values as needed.

If you are using the public OpenAI API directly, you may remove the base_url override or change it to the official endpoint per the OpenAI SDK instructions, and ensure pricing reflects the actual model you use.


## Troubleshooting
- Missing API key: The scripts raise KeyError("Missing API Key. Check your .env file.") when OPENAI_API_KEY is not set or visible. Ensure .env is in the working directory and contains the key, or set the environment variable directly.
- Path on Windows: If running from an IDE or different working directory, ensure the relative path to .env is correct. The scripts include commented examples for manually specifying the .env path.
- Network access: Ensure your environment can reach the configured base_url and that your key is valid for it.
- Dependencies: Make sure you installed from requirements_project.txt.


## Notes on repository tracking
- Only the file simple_cli_AI_chatbot.py is tracked inside the task directory; other Python files in that directory are ignored by .gitignore as part of the course scaffolding.
- requirements.txt is intentionally ignored; requirements_project.txt is the source of truth for dependencies.


## License
Provide your preferred license here (e.g., MIT). If omitted, assume all rights reserved by default.
