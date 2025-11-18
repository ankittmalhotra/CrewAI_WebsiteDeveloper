import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure using the key from your .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Checking available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f" - {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")