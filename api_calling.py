from google import genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS

# Loading the environment variable
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

#Initialization a Client
client = genai.Client(api_key=api_key)

# Note / Summary Generator
def note_generator(images):

    prompt = """Summarize the image in clear note format in (maximum 100 words). Use appropriate Markdown to separate and organize different sections."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text


# Audio Transcription
def audio_transcription(text):
    speech = gTTS(text, lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    # audio_buffer.seek(0)
    return audio_buffer 

# Generate Quiz
def quiz_generator(images, difficulty):

    prompt= f"Generate 3 quizzes base on the {difficulty}. Make sure to add markdown way. Last add also right answer."

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )

    return response.text