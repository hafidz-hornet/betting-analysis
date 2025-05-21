import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection details from environment variables
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_DATABASE')

# Create the connection engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

# Define your query
query = """
SELECT user_id, nickname, introduction, short_introduction, created_at
FROM tama_api.users
WHERE introduction LIKE '%%casino%%'
   OR nickname LIKE '%%casino%%'
   OR short_introduction LIKE '%%casino%%'
"""

# Execute the query and save to DataFrame
df = pd.read_sql(query, engine)

# Save to CSV
output_file = 'casino_users.csv'
df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"Query completed and saved to {output_file}")
