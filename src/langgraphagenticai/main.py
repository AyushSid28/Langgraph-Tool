import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.LLMS.openaillm import OpenAILLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the langgraph AgenticAI application with Streamlit UI.
    This function initialzes the UI,handles user input,configures the LLM model
    sets up the graph based on the selected use case and displays the output.
    implementing exception handling for robustness.
    """

    ui=LoadUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return

    user_message=st.chat_input("Enter your message here")

    if user_message:
        try:
            # Select LLM based on user choice
            selected_llm = user_input.get("selected_llm", "Groq")
            if selected_llm == "Groq":
                obj_llm_config = GroqLLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()
            elif selected_llm == "OpenAI":
                obj_llm_config = OpenAILLM(user_controls_input=user_input)
                model = obj_llm_config.llm_model()
            else:
                st.error(f"Error: Unsupported LLM selected: {selected_llm}")
                return

            if not model:
                st.error("Error: LLM model could not be initialised")
                return

            usecase=user_input.get("selected_usecase")

            if not usecase:
                st.error("Error:No use case selected")
                return


            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Failed to setup the graph: {e}")
                return 

            

            

        except Exception as e:
            st.error(f"Error: Failed to load the application: {e}")
            return

