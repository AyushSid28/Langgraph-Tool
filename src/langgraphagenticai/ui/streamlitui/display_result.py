import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
import json
from pprint import pprint

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message

        if usecase=="Basic Chatbot":
            # Display user message
            with st.chat_message("user"):
                st.write(user_message)
            
            # Stream the graph response
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                full_response = ""
                
                for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                    # Print complete event dictionary to terminal
                    print("\n" + "="*80)
                    print("STREAM EVENT (Complete Dictionary):")
                    print("="*80)
                    # Convert to serializable format for printing
                    event_dict = {}
                    for node_name, node_output in event.items():
                        event_dict[node_name] = {}
                        # Copy all fields from node_output
                        for key, value in node_output.items():
                            if key == 'messages':
                                # Convert messages to dict format for better readability
                                messages_list = []
                                for msg in value:
                                    msg_dict = {
                                        'type': type(msg).__name__,
                                        'content': getattr(msg, 'content', None),
                                        'id': getattr(msg, 'id', None),
                                        'additional_kwargs': getattr(msg, 'additional_kwargs', {}),
                                        'response_metadata': getattr(msg, 'response_metadata', None) if hasattr(msg, 'response_metadata') else None
                                    }
                                    messages_list.append(msg_dict)
                                event_dict[node_name]['messages'] = messages_list
                            else:
                                # Try to convert other fields, fallback to string representation
                                try:
                                    json.dumps(value)  # Test if serializable
                                    event_dict[node_name][key] = value
                                except (TypeError, ValueError):
                                    event_dict[node_name][key] = str(value)
                    
                    # Print with proper formatting
                    print(json.dumps(event_dict, indent=2, default=str))
                    print("="*80 + "\n")
                    
                    # Process for UI display
                    for node_name, node_output in event.items():
                        if 'messages' in node_output:
                            messages = node_output['messages']
                            if messages:
                                # Get the last message (AI response)
                                last_message = messages[-1]
                                if hasattr(last_message, 'content'):
                                    full_response = last_message.content
                                    response_placeholder.write(full_response)
                
                # Final response display
                if full_response:
                    response_placeholder.write(full_response)