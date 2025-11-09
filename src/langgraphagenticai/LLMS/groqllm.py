import os 
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input

    def get_llm_model(self):
        try: 
            groq_api_key=self.user_controls_input.get("GROQ_API_KEY", "") or os.getenv("GROQ_API_KEY", "")
            selected_groq_model=self.user_controls_input["selected_model"]
            if not groq_api_key:
                 st.error("GROQ API Key is not set")
                 raise ValueError("GROQ API Key is required. Please provide it in the UI or set GROQ_API_KEY environment variable.")

            llm=ChatGroq(api_key=groq_api_key,model=selected_groq_model)
        
        except Exception as e:
            raise ValueError(f"Error in getting the LLM model: {e}")

        return llm