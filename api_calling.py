from google import genai
from dotenv import load_dotenv
import os

# Loading the environment variable
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

#Initialization a Client
client = genai.Client(api_key=api_key)

# Note / Summary Generator
def note_generator(images):

    prompt = """Summarize the image in clear note format in Bangla(maximum 100 words). Use appropriate Markdown to separate and organize different sections."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text