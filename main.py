# from langchain_openai import ChatOpenAI

# from langchain import google_genai

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["Gemini"]=os.getenv("GEMINI_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("Langchain_api")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a assistant, Respond to each query"),
        ("user","Question:{question}")
    ]
)

st.title("SmartChat: LangChain × Gemini Flash")
input_text=st.text_input("Type the Question")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7,
google_api_key=os.environ["Gemini"]                             )
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))