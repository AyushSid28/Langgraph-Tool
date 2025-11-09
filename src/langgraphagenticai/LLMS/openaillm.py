import os
import streamlit as st
from langchain_openai import ChatOpenAI

class OpenAILLM:
    def __init__(self,user_controls_input):
       self.user_controls_input=user_controls_input
    

    def llm_model(self):
        try:
            openai_api_key=self.user_controls_input.get("OPENAI_API_KEY", "") or os.getenv("OPENAI_API_KEY", "")
            selected_model=self.user_controls_input['selected_model']
            if not openai_api_key:
                st.error("OPEN AI API KEY is not given")
                raise ValueError("OpenAI API Key is required. Please provide it in the UI or set OPENAI_API_KEY environment variable.")

            llm=ChatOpenAI(api_key=openai_api_key,model=selected_model)

        except Exception as e:
            raise ValueError(f"Error in getting the LLM model: {e}")

        return llm


