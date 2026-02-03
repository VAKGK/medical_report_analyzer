import google.generativeai as genai
import streamlit as st  # <--- 1. ADD THIS IMPORT

# --- 2. LOAD KEY FROM SECRETS (Secure Way) ---
# This works both Locally and on Streamlit Cloud
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except FileNotFoundError:
    # Fallback just in case the file is missing during local dev
    st.error("Secrets file not found. Please set up .streamlit/secrets.toml")
    API_KEY = ""

genai.configure(api_key=API_KEY)

def get_working_model_name():
    """
    Dynamically finds a working model to prevent 404 errors.
    """
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                if 'flash' in m.name: return m.name
                if 'pro' in m.name: return m.name
        return "models/gemini-pro"
    except:
        return "models/gemini-pro"


def analyze_medical_report(extracted_text):
    model_name = get_working_model_name()
    model = genai.GenerativeModel(model_name)

    # --- UPDATED PROMPT WITH VISUAL INDICATORS ---
    prompt = f"""
    You are an empathetic and smart medical assistant. Your job is to explain a lab report to a non-medical user clearly and visually.

    Extracted Text:
    "{extracted_text}"

    Please provide the analysis in this exact format:

    1. **Patient & Date:** (Extract if available, else "Not specified")

    2. **Summary of Tests (Table):**
       Create a Markdown table with columns: **Test Name**, **Result**, **Reference Range**, and **Status**.

       **CRITICAL RULE FOR STATUS COLUMN:**
       - If the result is **High**, write: "🔴 HIGH ⬆️"
       - If the result is **Low**, write: "🔵 LOW ⬇️"
       - If the result is **Normal**, write: "🟢 NORMAL ✅"

    3. **Key Insights (What matters):**
       - List ONLY the abnormal (High/Low) values.
       - Explain *why* it matters in 1 simple sentence. (e.g., "🔴 **High Glucose:** This suggests your blood sugar is up, which can be a sign of pre-diabetes.")

    4. **Simple Conclusion:**
       - A friendly 2-3 sentence summary of their overall health.
       - Use reassuring language.

    5. **Wellness Tips:**
       - 3 simple lifestyle tips relevant to these specific results (diet, sleep, or exercise).

    **Disclaimer:** Always end with: "I am an AI, not a doctor. Please consult a professional for a medical diagnosis."
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error with model '{model_name}': {e}"