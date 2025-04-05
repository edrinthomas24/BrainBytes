import streamlit as st
from utils.ocr_utils import extract_text_from_image
from PIL import Image

st.title("📝 OCR - Handwriting to Text")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    text = extract_text_from_image(image)
    st.text_area("Extracted Text:", text, height=300)

