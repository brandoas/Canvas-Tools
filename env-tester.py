import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_URL = os.getenv("API_URL")
COURSE_ID = os.getenv("COURSE_ID")

# Basic checks to ensure everything is loaded
if not ACCESS_TOKEN:
    raise ValueError("Missing ACCESS_TOKEN! Check your .env file.")
if not API_URL:
    raise ValueError("Missing API_URL! Check your .env file.")
if not COURSE_ID:
    raise ValueError("Missing COURSE_ID! Check your .env file.")
