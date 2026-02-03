import google.generativeai as genai

# PASTE YOUR KEY HERE
api_key = "AIzaSyBQWfp5kbTFnV6k3R7BoYlssAfXdxA7LLY"


genai.configure(api_key=api_key)

print("--- Checking Available Models ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Available: {m.name}")
except Exception as e:
    print(f"❌ Error: {e}")