# 🩺 VitalSense AI

### **Your Intelligent Medical Report Translator**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

---

## 📖 Overview

**Medical lab reports are confusing.** They are filled with complex jargon, numerical ranges, and abbreviations that leave patients anxious and unsure about their health.

**VitalSense AI** bridges this gap. It is an end-to-end **Hybrid AI application** that transforms dense, static medical reports into clear, actionable, and human-readable summaries.

By combining **Deep Learning for Computer Vision (OCR)** to "read" the document and **Generative AI (LLMs)** to "understand" the context, VitalSense empowers users with instant health insights.

> *"Making complex diagnostics accessible to everyone."*

---

## ✨ Key Features

* **📄 Multi-Format Support:** Seamlessly analyzes both high-quality PDFs and common image formats (JPG, PNG).
* **👁️ Hybrid OCR Engine:** Utilizes a specialized pipeline (Poppler + EasyOCR) optimized for speed and accuracy on dense documents.
* **🧠 Intelligent Analysis:** Leverages **Google Gemini 1.5 Pro/Flash** to interpret medical data with high context awareness.
* **🚦 Visual Status Indicators:** Instantly flags results with intuitive visual cues:
    * 🔴 **HIGH**
    * 🔵 **LOW**
    * 🟢 **NORMAL**
* **🔒 Privacy-First Design:** All data is processed in-memory and is never stored on a server.

---

## ⚙️ How it Works (The Architecture)

VitalSense AI is a sophisticated **ETL (Extract, Transform, Load)** pipeline designed for unstructured medical data.

```mermaid
graph TD;
    A[📄 User Uploads Report\nPDF/Image] --> B{🖼️ Preprocessing};
    B -->|CV & Poppler| C[🧹 Cleaned Image Arrays];
    C -->|Deep Learning OCR\nEasyOCR| D[📝 Raw Extracted Text];
    D -->|Prompt Engineering| E{🤖 Generative AI\nGoogle Gemini};
    E -->|Structured Analysis| F[📊 Final Streamlit UI\nSimple Summary & Data Table];

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px
