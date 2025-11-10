Langgraph Agentic AI Chatbot

This is a stateful agentic AI chatbot application built using LangGraph and Streamlit. The application provides two modes of operation: a basic chatbot and an advanced chatbot with web search capabilities.

Features

Basic Chatbot Mode
A simple conversational chatbot that uses LLM models to generate responses based on user input. Supports both Groq and OpenAI models.

Chatbot with Web Search
An advanced chatbot that integrates with Tavily Search API to provide real-time web search capabilities. The chatbot can search the web for current information and incorporate search results into its responses.

Architecture

The application uses LangGraph to build stateful conversational graphs. The graph structure includes:

- Chatbot Node: Processes user messages and generates AI responses
- Tool Node: Executes web search operations using Tavily
- Conditional Routing: Automatically routes to tools when needed or ends conversation when appropriate

The graph flow starts with the user message, routes through the chatbot node, conditionally calls the tool node for web searches, and returns to the chatbot node to generate a final response incorporating the search results.

Tavily Search Tool

The application uses Tavily Search API for web search functionality. Tavily is a search API that provides real-time web search results. The tool is integrated using LangChain's TavilySearchResults wrapper, which allows the chatbot to search the web and retrieve relevant information to enhance its responses.

When a user asks a question that requires current information, the chatbot automatically calls the Tavily search tool, retrieves relevant web results, and incorporates this information into its response.

Setup

The application requires API keys for:
- LLM Provider: Either Groq API key or OpenAI API key
- Tavily API key: Required for the Chatbot with Web Search mode

The application is built with Python and uses Streamlit for the user interface. All dependencies are managed through standard Python package management.

Usage

Run the Streamlit application and select your preferred LLM model and use case. For web search functionality, ensure you have a valid Tavily API key configured in the sidebar.

