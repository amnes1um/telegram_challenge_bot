import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("tg_api_token")
admin_id = os.getenv("admin_id")
