import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

# 1. Load CSV into DataFrame
csv_file_path = "spamham.csv"  
df = pd.read_csv(csv_file_path)

# 2. Connect to MongoDB
mongo_uri = os.getenv("MONGO_DB_URL")  
client = MongoClient(mongo_uri)

# 3. Access DB and Collection
db = client["Spam_Detection"]     
collection = db["Spam_Ham"] 

# 4. Upload data
data = df.to_dict(orient="records")  
collection.insert_many(data)

print(f"Inserted {len(data)} documents into MongoDB collection!")
