import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('LLM_API_KEY')
BASE_URL = os.getenv('LLM_BASE_URL')
MODEL = os.getenv('LLM_MODEL')
