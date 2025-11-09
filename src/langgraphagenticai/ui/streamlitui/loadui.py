import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}


    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(),layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
          llm_options=self.config.get_llm_options()
          usecase_options=self.config.get_use_case_options()

          self.user_controls["selected_llm"]=st.selectbox("Select LLM",llm_options)
          if self.user_controls["selected_llm"]=="Groq":
            model_options=self.config.get_groq_model_options()
            self.user_controls["selected_model"]=st.selectbox("Select Model",model_options)
            if "GROQ_API_KEY" not in st.session_state:
                st.session_state["GROQ_API_KEY"] = ""
            self.user_controls["GROQ_API_KEY"]=st.text_input("Enter GROQ API key",value=st.session_state.get("GROQ_API_KEY",""),type="password", key="groq_key")
            st.session_state["GROQ_API_KEY"] = self.user_controls["GROQ_API_KEY"]
            if not self.user_controls["GROQ_API_KEY"]:
                st.warning("Please enter your GROQ API Key to continue.Don't have? refer https://groq.com/docs/api-reference/authentication")
          elif self.user_controls["selected_llm"]=="OpenAI":
            model_options=self.config.get_openai_model_options()
            self.user_controls["selected_model"]=st.selectbox("Select Model",model_options)
            if "OPENAI_API_KEY" not in st.session_state:
                st.session_state["OPENAI_API_KEY"] = ""
            self.user_controls["OPENAI_API_KEY"]=st.text_input("Enter OpenAI API key",value=st.session_state.get("OPENAI_API_KEY",""),type="password", key="openai_key")
            st.session_state["OPENAI_API_KEY"] = self.user_controls["OPENAI_API_KEY"]
            if not self.user_controls["OPENAI_API_KEY"]:
                st.warning("Please enter your OpenAI API Key to continue.Don't have? refer https://platform.openai.com/api-keys")
        #Usecase selection
          self.user_controls["selected_usecase"]=st.selectbox("Select the usecase",usecase_options)

        return self.user_controls