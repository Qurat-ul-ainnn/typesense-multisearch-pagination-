"""
config.py

Configuration file for API settings.

IMPORTANT:
Do NOT hardcode API keys in this file.
Use environment variables instead.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

API_KEY = os.getenv("TYPESENSE_API_KEY")

PER_PAGE = 250  # Adjust based on API limits

HEADERS = {
    "accept": "application/json",
    "content-type": "text/plain",
    "x-typesense-api-key": API_KEY
}
