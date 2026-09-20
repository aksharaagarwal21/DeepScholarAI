import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    # Load variables from the .env file
    load_dotenv()

    # Read the API key
    api_key = os.getenv("OPENAI_API_KEY")

    # Make sure the key exists
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY was not found. Check your .env file."
        )

    # Create a connection to the OpenAI API
    client = OpenAI(api_key=api_key)

    print("DeepScholar AI is starting...\n")

    # Send our first request to an LLM
    response = client.responses.create(
        model="gpt-5.6-luna",
        input="Explain machine learning.Requirements:- Exactly 5 sentences- Use simple language- Give one example"
    )

    # Display the generated text
    print("DeepScholar:")
    print(response.output_text)


if __name__ == "__main__":
    main()