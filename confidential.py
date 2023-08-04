
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# # Access the environment variables
api_key = os.getenv('API_KEY')
database_password = os.getenv('DATABASE_PASSWORD')
print(api_key,database_password)
