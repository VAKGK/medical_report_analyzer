import streamlit as st
from src.ocr_engine import extract_text_from_image, extract_text_from_pdf
from src.llm_engine import analyze_medical_report

# 1. Page Config
st.set_page_config(
    page_title="VitalSense AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS
st.markdown("""
    <style>
    /* Table Styling */
    table {
        width: 100% !important;
        table-layout: auto !important;
    }
    th, td {
        padding: 12px !important;
        text-align: left !important;
    }
    th:last-child, td:last-child {
        min-width: 150px !important;
        white-space: nowrap !important;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B; 
        color: white;
        font-size: 18px;
        padding: 10px;
        border-radius: 10px;
    }

    /* Sidebar Step Cards */
    .sidebar-card {
        background-color: #262730; /* Darker background for contrast if dark mode */
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #444;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Navigation & Guide)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004458.png", width=80)
    st.title("VitalSense AI")
    st.caption("Your Personal Health Translator")

    st.markdown("---")

    # --- MOVED: HOW IT WORKS (Vertical Layout) ---
    st.subheader("🚀 How it Works")

    st.markdown("#### 📂 Step 1: Upload")
    st.caption("Upload your lab test image or PDF.")

    st.markdown("#### 🧠 Step 2: Analyze")
    st.caption("Our AI scans and interprets the data.")

    st.markdown("#### ✅ Step 3: Summary")
    st.caption("Get a simple, plain-English report.")

    st.markdown("---")

    # --- UPDATED DISCLAIMER ---
    st.warning("⚠️ **Educational Use Only**")
    st.caption(
        "This project is created for **study purposes only**."
        "\n\nDo NOT use this for real medical decisions. Always consult a doctor."
    )

    st.info("🔒 **Privacy:** Data is processed in memory and not saved.")

# 4. Main Page Content
st.title("🩺 AI Medical Report Analyzer")
st.markdown("### Decode your lab report in seconds.")
st.write("Upload your medical report below to get a clear, easy-to-understand summary of your health vitals.")

st.markdown("---")

# 5. File Upload Section
uploaded_file = st.file_uploader(
    "📂 Upload your report here (PDF, PNG, JPG)",
    type=['pdf', 'png', 'jpg', 'jpeg']
)

if uploaded_file is not None:

    # Optional Preview (Clean Dropdown)
    with st.expander("👀 View Uploaded File (Click to Expand)", expanded=False):
        if uploaded_file.type == "application/pdf":
            st.info(f"✅ **PDF Uploaded:** {uploaded_file.name}")
        else:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Analyze Button
    analyze_btn = st.button("✨ Analyze Report Now")

    # Results Section
    if analyze_btn:
        with st.spinner("🔍 Reading document..."):
            try:
                if uploaded_file.type == "application/pdf":
                    extracted_text = extract_text_from_pdf(uploaded_file)
                else:
                    extracted_text = extract_text_from_image(uploaded_file)
            except Exception as e:
                st.error(f"❌ Error reading file: {e}")
                extracted_text = None

        if extracted_text:
            with st.spinner("🧠 AI is analyzing your health data..."):
                try:
                    analysis = analyze_medical_report(extracted_text)
                    st.balloons()

                    st.success("Analysis Complete!")

                    # Layout: Simple Summary vs Raw Data
                    tab1, tab2 = st.tabs(["✨ Simple Summary", "🔍 Raw Data"])

                    with tab1:
                        st.markdown(analysis)
                        st.info("💡 **Tip:** This is an AI-generated summary for educational purposes.")

                    with tab2:
                        with st.expander("Show Extracted Text"):
                            st.text(extracted_text)

                except Exception as e:
                    st.error(f"❌ AI Analysis Failed: {e}")