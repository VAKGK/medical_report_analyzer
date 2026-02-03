import easyocr
import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image
from src.utils import preprocess_image
import os
import numpy as np


@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'], gpu=False)


def extract_text_from_image(image_file):
    image = Image.open(image_file)
    processed_img = preprocess_image(image)
    reader = load_reader()
    result = reader.readtext(processed_img, detail=0)
    return " ".join(result)


def extract_text_from_pdf(pdf_file):
    base_path = os.getcwd()
    poppler_path = os.path.join(base_path, "poppler-24.02.0", "Library", "bin")

    # Notify the user
    st.write("Processing PDF... (Fast Mode)")

    # 1. SPEED BOOST: Lower DPI + Grayscale
    images = convert_from_bytes(
        pdf_file.read(),
        dpi=150,  # 150 is much faster than 300
        grayscale=True,  # Black & white is faster to process
        fmt='jpeg',
        poppler_path=poppler_path
    )

    full_text = ""
    reader = load_reader()

    # Progress bar for better UX
    progress_bar = st.progress(0)

    for i, image in enumerate(images):
        # 2. SPEED BOOST: Skip heavy preprocessing for clean digital PDFs
        # Just convert directly to numpy array
        img_array = np.array(image)

        result = reader.readtext(img_array, detail=0)
        page_text = " ".join(result)
        full_text += f"\n--- Page {i + 1} ---\n{page_text}"

        # Update progress
        progress_bar.progress((i + 1) / len(images))

    return full_text