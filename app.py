import os
import streamlit as st
from PIL import Image
import pytesseract
from transformers import AutoProcessor, Qwen2VLForConditionalGeneration
import torch
import re

# Set Tesseract data path and OCR languages (English + Hindi)
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'  
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
tesseract_config_multi = '--psm 6 -l eng+hin'

# Load model and processor
@st.cache_resource
def load_model():
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen2-VL-2B-Instruct", trust_remote_code=True, torch_dtype=torch.bfloat16
    ).cuda().eval()
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct", trust_remote_code=True)
    return model, processor

# Streamlit app
def main():
    st.title("Optical Character Recognition (OCR) Application")

    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract text using Tesseract OCR
        extracted_text = pytesseract.image_to_string(image, config=tesseract_config_multi)
        st.write("**Extracted Text from Image:**")
        st.write(extracted_text)

        # Search keyword in extracted text
        keyword = st.text_input("Enter a keyword to search:")
        if keyword:
            matches = re.finditer(rf"\b{keyword}\b", extracted_text, re.IGNORECASE)
            match_positions = [match.start() for match in matches]

            if match_positions:
                st.write(f"Keyword '{keyword}' found at positions: {match_positions}")
                highlighted_text = highlight_keywords(extracted_text, keyword)
                st.markdown(highlighted_text, unsafe_allow_html=True)
            else:
                st.write(f"No occurrences of '{keyword}' found.")

# Highlight keyword in text
def highlight_keywords(text, keyword):
    return re.sub(rf"\b({keyword})\b", r"<span style='color: red; font-weight: bold;'>\1</span>", text, flags=re.IGNORECASE)

if __name__ == "__main__":
    main()
