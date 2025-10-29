import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadUI:
    def __init__(self):
        self.config=Config()
        self.usercontrol={}


    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(),layout="wide")

        with st.sidebar:
          llm_options=self.config.get_llm_options()
          usecase_options=self.config.get_use_case_options()

          self.user_control["selected_llm"]=st.selectbox("Select LLM",llm_options)
          