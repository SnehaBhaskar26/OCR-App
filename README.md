
---

# OCR and Document Search Web Application

**Live URL**: [https://3n4cdipvkuvrbboj4jurzk.streamlit.app/]
## Demo

Click the image below to watch the demo video:

![Watch the Demo](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*EVqdhNOB55c_GT95)

Or click [here](https://drive.google.com/file/d/1tW9Eo_MXWY-V3ggH5R_6e5nG085HDWrl/view?usp=drive_link) to watch the demo directly.


## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation and Setup](#installation-and-setup)
5. [How to Use the Application](#how-to-use-the-application)
7. [Deployment](#deployment)
8. [File Structure](#file-structure)
9. [Contact Information](#contact-information)


## Project Overview

This project is a **web-based OCR (Optical Character Recognition) and Document Search prototype**. It allows users to upload an image containing text in both **Hindi** and **English**, extracts the text using an OCR model, and performs keyword searches on the extracted text. The application highlights the occurrences of the searched keywords and returns their positions in the text.

The app is developed using **Streamlit** for the front-end interface, **Pytesseract** for OCR, and **Huggingface Transformers** for advanced text processing, particularly using the **Qwen2-VL-2B-Instruct** model. It supports JPEG and PNG image formats.

## Features

- **Upload an Image**: Users can upload an image (JPEG/PNG) containing text in Hindi and English.
- **OCR Functionality**: Extracts text from the uploaded image using Pytesseract and Huggingface's Qwen2-VL-2B-Instruct model.
- **Keyword Search**: Users can search for specific keywords within the extracted text.
- **Highlighted Search Results**: Any keyword found in the extracted text is highlighted with its positions displayed.
- **Multi-language Support**: Handles both **Hindi** and **English** text.

## Tech Stack

- **Python**: Core language for building the application.
- **Streamlit**: For building the user interface.
- **Pytesseract**: For OCR processing.
- **Huggingface Transformers**: For handling the OCR model.
- **Regular Expressions (Regex)**: For searching and highlighting keywords.

## Installation and Setup

To run this project locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- `tesseract-ocr` installed on your system. You can install it from [here](https://github.com/tesseract-ocr/tesseract).

### Clone the Repository

```bash
git clone https://github.com/SnehaBhaskar26/OCR-App.git
cd OCR-App
```

### Setting up the Environment

1. **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv ocr_env
    source ocr_env/bin/activate
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Tesseract**:
    Make sure to install Tesseract and set its path:
    - On **Linux**: Use your package manager (e.g., `sudo apt-get install tesseract-ocr`).
    - On **Windows**: Download and install it from [here](https://github.com/UB-Mannheim/tesseract/wiki).
    - Add the Tesseract executable path to your `PATH` environment variable.

4. **Set the Tesseract data path in your code**:
   Ensure that the correct path to your Tesseract installation is set in the `app.py` file:
   ```python
   os.environ['TESSDATA_PREFIX'] = '/path/to/tessdata'
   pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'
   ```

### Running the Application

After setting up the environment, run the following command to launch the Streamlit app:

```bash
streamlit run app.py
```

This will start the application, and you can access it on your local browser at `http://localhost:8501`.

## How to Use the Application

1. **Upload Image**: Click on the "Upload an Image" button and select an image (JPEG/PNG) containing text in Hindi or English.

![image](https://github.com/user-attachments/assets/9552a65f-6c0a-4253-8869-d59b785f4224)





  
2. **Extracted Text**: The application will extract and display the text from the uploaded image.


![image](https://github.com/user-attachments/assets/dab62936-c053-4d13-a4f1-97379b98ce00)




   
3. **Keyword Search**: Enter a keyword in the search box to find occurrences of that keyword in the extracted text.

![image](https://github.com/user-attachments/assets/b2c3c029-ea0c-4728-905c-f1a5c91c4f93)





4. **Highlighted Results**: If the keyword is found, it will be highlighted in the text along with the positions.

![image](https://github.com/user-attachments/assets/2129a50b-061e-4516-980a-ff9a7cef1475)



   


## Deployment

The application can be deployed on platforms such as **Streamlit Sharing** or **Hugging Face Spaces**.

### Deployment on Streamlit Sharing

1. **Create a Streamlit Sharing account**: [Streamlit Cloud](https://streamlit.io/cloud)
2. **Push the code to GitHub**: Ensure your repository is up to date.
3. **Deploy**: On Streamlit Cloud, create a new app and link your GitHub repository. Streamlit will automatically deploy your app.

After deployment, your app will be accessible via a public URL, which you can share.


## File Structure

```
|-- app.py            # Main Python script for the web application
|-- README.md         # Documentation file
|-- requirements.txt  # List of dependencies
```
## Contact Information

If you have any questions or would like to get in touch, feel free to contact me:

- **Name**: Sneha Bhaskar
- **Email**: bhaskarsneha2923@gmail.com
- **LinkedIn**: [https://www.linkedin.com/in/snehabhaskar]
- **GitHub**: [https://github.com/SnehaBhaskar26]




---

