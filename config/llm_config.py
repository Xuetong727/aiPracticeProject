import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL", "https://api.deepseek.com")
model = os.getenv("MODEL", "deepseek-v4-pro")
