# importing necessary modules 
import streamlit as st 
import google.generativeai as genai
from PIL import Image
import key_scrt #gen-ai api_key

# Configuring GenAI API
genai.configure(api_key=key_scrt.GOOGLE_API_KEY)

# Function to interact with GenAI model
def get_gemini(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')  # specifying the model
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app 
st.set_page_config(page_title="Descriptive AI", page_icon=":bulb:")
st.title("Gemini Application")
st.markdown("---")

# Input fields
input_text = st.text_input("Enter Prompt: ", key="input")
st.markdown("---")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
submit_button = st.button("Analyze")

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.markdown("---")

# Perform analysis on button click
if submit_button:
    if uploaded_file is None:
        st.error("Please upload an image.")
    else:
        response = get_gemini(input_text, image)
        st.subheader("Result")
        st.write(response)


