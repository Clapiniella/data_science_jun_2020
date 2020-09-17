from flask import Flask, request
from src.config import PORT
from src.gitapi import getBySeniority, requestUsers
from src.predict import predictUser
from src.scraper import getLinks

app = Flask(__name__)


@app.route("/")
def baseResponse():
    return {
        "Hello welcome to Venandi! This API has 2 basic tasks": 
        {
        "1":{"Find Github users by location, programming language and seniority: to perform this query use the following command": "/user/<location>/<language>/<seniority>/get"}, 
        "2":{"Predict the seniority of the selected user": "to perform this query use the following command: /user/<login>/predict"}
        }}

@app.route("/user/<location>/<language>/<seniority>/get", methods=["GET"])
def searchUser(location, language, seniority):
    user_chars = {"location":location, "language":language, "seniority":seniority}
    followers, repos = getBySeniority(user_chars["seniority"])
    users = requestUsers(user_chars["location"], user_chars["language"], followers, repos)
    return users


@app.route("/user/<login>/predict", methods=["GET"])
def recommend(login):
    seniority = predictUser(login)
    links = getLinks(login)
    return {"Github Seniority":seniority, "Linkedin Profile Link & could happen Social Media links":links}
    

