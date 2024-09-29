import os
import streamlit as st
from PIL import Image
import pytesseract
from transformers import AutoProcessor, Qwen2VLForConditionalGeneration
import torch
import re

# Set TESSDATA_PREFIX environment variable for Tesseract
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/'  # Adjust the path if needed

# Configure Tesseract to use both English and Hindi OCR
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Ensure this path is correct
tesseract_config_multi = '--psm 6 -l eng+hin'  # Config for recognizing both English and Hindi

# Load the Qwen2VL model (if needed for additional tasks like querying, beyond OCR)
@st.cache_resource
def load_model():
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen2-VL-2B-Instruct", trust_remote_code=True, torch_dtype=torch.bfloat16
    ).cuda().eval()
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct", trust_remote_code=True)
    return model, processor

# Main application function
def main():
    st.title("Multilingual Image-to-Text & Query Processing Application")

    # Step 1: Image upload
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        # Step 2: Display uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Step 3: Extract text using Tesseract OCR with English + Hindi config
        extracted_text = pytesseract.image_to_string(image, config=tesseract_config_multi)

        # Step 4: Display the extracted text in its native script (English and Hindi)
        st.write("**Extracted Text from Image:**")
        st.write(extracted_text)  # This will show both English and Hindi text

        # Step 5: Ask for user query to search for keywords in the extracted text
        keyword = st.text_input("Enter a keyword to search in the extracted text:")

        if keyword:
            # Find matches for the keyword in the extracted text
            matches = re.finditer(rf"\b{keyword}\b", extracted_text, re.IGNORECASE)
            match_positions = [match.start() for match in matches]

            if match_positions:
                st.write(f"*Keyword '{keyword}' found at positions:* {match_positions}")
                highlighted_text = highlight_keywords(extracted_text, keyword)
                st.markdown(highlighted_text, unsafe_allow_html=True)
            else:
                st.write(f"No occurrences of '{keyword}' found in the extracted text.")

# Function to highlight keywords in extracted text
def highlight_keywords(text, keyword):
    # Use <span> with inline CSS to highlight keywords in red
    highlighted_text = re.sub(rf"\b({keyword})\b", r"<span style='color: red; font-weight: bold;'>\1</span>", text, flags=re.IGNORECASE)
    return highlighted_text

# Run the application
if __name__ == "__main__":
    main()
