import json
import requests
import os
from dotenv import load_dotenv
import time
from math import ceil
#from mongodb import addProfile --> (we let it commented as we won't use it after the seniority classes are found)
from src.constants import countries, followers, seniority_dict
import pandas as pd



def getFromGithub(path, params):
    load_dotenv()

    apiKey = os.getenv("github")

    # Construct the resource url
    url = f"https://api.github.com/{path}"
    
    # If apiKey is defined, pass a header
    headers = {"Authorization":f"token {apiKey}"} if apiKey else {}

    # Perform the request
    res = requests.get(url, params=params, headers=headers)
    print(res.status_code, res.url)

    
    # Extract json from body response
    return res.json()



def getUsers(countries, followers):
    count_hour = 0
    counter = 0
    users = []
    for c in countries:
        for f in followers:
            count_hour +=1
            counter +=1
            if counter == 30:
                print("paradita")
                time.sleep(61)                      
                counter = 0
            elif 4975 <= count_hour <= 5000:
                print("paradita")
                time.sleep(3601)                      
                count_hour = 0
            else: 
                total = getFromGithub("search/users?", f"q=location:{c}+followers:{f}&per_page=100")["total_count"]              
            if total >= 1000:
                for p in range(1,11):
                    count_hour +=1
                    counter += 1               
                    if counter == 30:
                        print("paradita")
                        time.sleep(61)                   
                        counter = 0
                    elif 4975 <= count_hour <= 5000:
                        print("paradita")
                        time.sleep(3601)                      
                        count_hour = 0
                    else:
                        req = getFromGithub("search/users?", f"q=location:{c}+followers:{f}&page={p}&per_page=100")["items"]
                    for r in req:
                        users.append(r["login"])
            else:
                rango = ceil(total/100)
                for p in range(1,rango+1):
                    count_hour +=1
                    counter += 1                    
                    if counter == 30:
                        print("paradita")
                        time.sleep(61)                     
                        counter = 0
                    elif 4975 <= count_hour <= 5000:
                        print("paradita")
                        time.sleep(3601)                      
                        count_hour = 0
                    else:
                        req = getFromGithub("search/users?", f"q=location:{c}+followers:{f}&page={p}&per_page=100")["items"]
                    for r in req:
                        users.append(r["login"])

    return list(set(users)), count_hour



def getInfo(countries, followers):
    profile_mongo = []
    counter = 0
    users, count_hour = getUsers(countries, followers)
    for u in users:
        print(count_hour)
        print(u)
        count_hour +=1
        counter +=1
        if counter == 30:
            print("paradita")
            time.sleep(61)                      
            counter = 0
        elif 4975 <= count_hour <= 5000:
            print("paradita")
            time.sleep(3601)                      
            count_hour = 0
        else: 
            total = getFromGithub(f"users/{u}","")["public_repos"]  
        if total <= 100:
            for p in range(1,2):
                count_hour += 2
                counter += 2
                if counter == 30:
                    print("paradita")
                    time.sleep(61)                      
                    counter = 0
                elif 4975 <= count_hour <= 5000:
                    print("paradita")
                    time.sleep(3601)                      
                    count_hour = 0
                else:
                    user = getFromGithub(f"users/{u}","")
                    repo = getFromGithub(f"users/{u}/repos?page={p}&per_page=100","")

                    repo_info = []
                    for r in repo:
                        repo_info.append({"repo_name":r["name"], "forked":r["fork"], "stars":r["stargazers_count"], "language":r["language"], "forks":r["forks_count"]})
                    profile = {"name":user["name"], "company":user["company"], "location":user["location"], "email":user["email"], "hireable":user["hireable"], 
                    "repos_number":user["public_repos"], "repos":repo_info, "followers":user["followers"], "created":user["created_at"], "updated":user["updated_at"]}
                    profile_mongo.append(profile)
                    print("ok")
                    
        else:
            rango = ceil(total/100)
            for p in range(1,rango+1):
                count_hour += 2
                counter += 2
                if counter == 30:
                    print("paradita")
                    time.sleep(61)                      
                    counter = 0
                elif 4975 <= count_hour <= 5000:
                    print("paradita")
                    time.sleep(3601)                      
                    count_hour = 0
                else:
                    user = getFromGithub(f"users/{u}","")
                    repo = getFromGithub(f"users/{u}/repos?page={p}&per_page=100","")

                    repo_info = []
                    for r in repo:
                        repo_info.append({"repo_name":r["name"], "forked":r["fork"], "stars":r["stargazers_count"], "language":r["language"], "forks":r["forks_count"]})
                    profile = {"name":user["name"], "company":user["company"], "location":user["location"], "email":user["email"], "hireable":user["hireable"], 
                    "repos_number":user["public_repos"], "repos":repo_info, "followers":user["followers"], "created":user["created_at"], "updated":user["updated_at"]}
                    profile_mongo.append(profile)
                    print("ok")
    return addProfile(profile_mongo)



def getBySeniority(seniority):
    followers = seniority_dict["followers"][seniority]
    repos = seniority_dict["repos"][seniority]
    return followers, repos



def requestUsers(location, language, followers, repos):
    users = getFromGithub("search/users?", f"q=location:{location}+language:{language}+followers:{followers}+repos:{repos}&per_page=100")["items"]
    login = []
    for u in users:
        login.append(u["login"])
    user_info = []
    for l in login:
        user = getFromGithub(f"users/{l}","")
        profile = {"1. Name":user["name"], "2. Company":user["company"], "3. Location":user["location"], "4. Email":user["email"], "5. Hireable":user["hireable"], 
                    "6. Number of Repositories":user["public_repos"], "7. Number of Followers":user["followers"], "8. Account Created at":user["created_at"], "9. Account Updated at":user["updated_at"]}
        user_info.append(profile)
    return {n:d for n,d in enumerate(user_info)}



def reqUser(login):
    user = getFromGithub(f"users/{login}","")
    profile = {"repos":user["public_repos"], "followers":user["followers"]}
    name = user["name"]
    location = user["location"]
    return pd.DataFrame(profile, index=[0]), name, location

