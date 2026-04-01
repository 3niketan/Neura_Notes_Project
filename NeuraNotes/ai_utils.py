import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_note(note):

    prompt = f"Summarize the following note in a concise way:\n{note}"

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text

def grammar_check(note):
    prompt = f"Correct the grammar of the following text and return only the corrected version:\n{note}"

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text

def title_generator(note):
    prompt = f"Generate a single short, meaningful title for the following note, don't give suggestions directly provide me single result:\n{note}"

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text

def tag_generator(note):
    prompt = f"""
Analyze the following content and generate exactly 5 relevant tags.

Guidelines:
- Tags should be short (1–3 words each)
- Focus on key topics, concepts, or themes
- Avoid generic words like "note", "text", "content"
- Output only the tags as a comma-separated list

Content:
\n{note}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text
def polish_generator(note):
    prompt = f"""
Rewrite and enhance the following note.

Rules:
- Generate exactly 2 variations
- Keep it concise and meaningful
- No extra text and not in json format

Return format:
"Version 1: text" 
"Version 2: text"


Content:
\n{note}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text