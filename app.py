import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name='gemini-pro-vision')


def get_response(input_text, image, prompt):
    response = model.generate_content([input_text, image, prompt])
    return response.text


st.set_page_config(page_title="Gemini Application")
st.title("Gemini Vision App")


input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)


input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice, and you will have to answer any question based on the invoice.
"""


if st.button("Tell me about the Invoice:"):
    if image and input_text:
        response = get_response(input_prompt, image, input_text)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please upload an image and enter a prompt.")
