import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    BASE_URL = os.getenv("BASE_URL")
    API_KEY = os.getenv("API_KEY")
