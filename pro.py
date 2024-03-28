#importing necessary modules 
import streamlit as st 
import google.generativeai as genai
import os 
import key_scrt #gen-ai api_key
genai.configure(api_key=key_scrt.GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')  #specifying the model
#Testing the gen-ai model 
# response=model.generate_content("Give a brief Explanati on about Astro Physics !")
# print(response.text)


def get_gemini(question):
    response=model.generate_content(question)
    return response.text

#Initilizing the stramlit app 
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the Question")

#when submit is clicked 
if submit:
    response=get_gemini(input)
    st.write(response)
    