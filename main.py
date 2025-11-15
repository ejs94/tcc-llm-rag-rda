import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

gemini_token = os.getenv("GEMINI_TOKEN")


def main():

    client = genai.Client(api_key=gemini_token)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how AI works in a few words",
    )

    print(response.text)


if __name__ == "__main__":
    main()
