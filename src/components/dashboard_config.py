import json
import streamlit as st

def save_dashboard_config(config):
    """
    Save user-defined dashboard configuration.
    """
    with open("dashboard_config.json", "w") as file:
        json.dump(config, file)

def load_dashboard_config():
    """
    Load user-defined dashboard configuration.
    """
    try:
        with open("dashboard_config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
