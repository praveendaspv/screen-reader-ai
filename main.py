import mss
import os
import time
from google import genai
from dotenv import load_dotenv

# 1. Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the client
client = genai.Client(api_key=api_key)

# 2. Capture Screen
def take_screenshot():
    # Use mss.MSS() to avoid the DeprecationWarning
    with mss.MSS() as sct:
        sct.shot(output="screenshot.png")

# 3. Analyze with AI
def analyze_screen():
    take_screenshot()
    
    # We use 'file' as the parameter name
    image_file = client.files.upload(file="screenshot.png")
    
    # Use a current, stable model name
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "What is on this screen and what should I do next?",
            image_file
        ]
    )
    print(response.text)

if __name__ == "__main__":
    analyze_screen()