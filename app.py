import streamlit as st
from src.app import render_application

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Black-Scholes Calculator",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def main():
    """
    Main entry point for the Streamlit application.
    """
    render_application()  # Call the function to render the main application

if __name__ == "__main__":
    main()
