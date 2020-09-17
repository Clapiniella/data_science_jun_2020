from src.config import db

def addProfile(user):
    coll = db["profiles"]
    return coll.insert_many(user)

    