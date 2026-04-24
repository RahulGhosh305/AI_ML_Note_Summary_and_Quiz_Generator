import google.generativeai as genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS

# Load env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Note / Summary Generator
def note_generator(images):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = """Summarize the image in clear note format (max 100 words).
Use proper Markdown headings and bullet points."""

    response = model.generate_content([prompt, images])

    return response.text


# Audio Transcription (Text → Speech actually)
def audio_transcription(text):
    speech = gTTS(text, lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer


# Generate Quiz
def quiz_generator(images, difficulty):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""Generate 3 quiz questions based on the image.
Difficulty: {difficulty}

Format:
- Use Markdown
- Add options (A, B, C, D)
- Mention correct answer at the end
"""

    response = model.generate_content([prompt, images])

    return response.text