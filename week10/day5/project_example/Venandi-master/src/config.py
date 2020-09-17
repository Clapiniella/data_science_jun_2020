#from pymongo import MongoClient
import os
import dotenv
dotenv.load_dotenv()

#we let mongo commented as we won't use it anymore once we have got the seniority classes
#MongoDB
"""MGURL = os.getenv("MGURL")
myclient = MongoClient(f"{MGURL}")
db = myclient["github"]"""

#Local Connection
PORT = os.getenv("PORT")