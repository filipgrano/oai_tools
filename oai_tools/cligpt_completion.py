import sys

import openai

from oai_tools import get_api_key, read_config
from oai_tools.cligpt import explain_command, generate_command

openai.api_key = get_api_key()
config = read_config()
cligpt_config = config.get("cligpt", {})
MODEL = cligpt_config.get("model", "gpt-3.5-turbo")
MAX_TOKENS_COMMAND = cligpt_config.get("max_tokens", {}).get("command", 100)
TEMPERATURE_COMMAND = cligpt_config.get("temperature", {}).get("command", 0.1)


def complete():
    try:
        prompt = " ".join(sys.argv[1:])
        completion_response = generate_command(prompt)
        completion = completion_response.choices[0].message.content.strip()
        print(completion)
    except KeyboardInterrupt:
        print("\nAborted by user.")


def explain():
    try:
        prompt = " ".join(sys.argv[1:])
        explanation_response = explain_command(prompt)
        explanation = explanation_response.choices[0].message.content.strip()
        print(explanation)
    except KeyboardInterrupt:
        print("\nAborted by user.")
