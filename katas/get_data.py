import requests
import json
import pandas as pd

with open("settings.json", "r+") as outfile:
    variable = json.load(outfile)

def get_completed_by_user(user, users=variable["USERS"], path=variable["COMPLETE"]):
    url = users + user + path
    resp = requests.get(url)    
    return resp.json()

def get_name_kata(id_kata, katas=variable["KATA"]):
    url = katas + id_kata
    resp = requests.get(url)
    return resp.json()

'''
def create_dataframe():
    return pd.DataFrame({"user":[],"kata_id":[], "kata_name":[], "when":[]})
'''

def fulfill_df(function_check_if_done, df_katas):
    # TODO: Raise error when the user doesn't exist
    new_row = {"user":function_check_if_done[0],"kata_id":function_check_if_done[1], "kata_name":function_check_if_done[2], "when":function_check_if_done[3]}
    #append row to the dataframe
    return df_katas.append(new_row, ignore_index=True)

def check_if_done(user, kata_id):
    name_kata = None
    time = False
    try:
        for i in range(len(get_completed_by_user(user)['data'])):
            name_kata = get_name_kata(kata_id)['name']
            if get_completed_by_user(user)['data'][i]['id'] == kata_id:
                time = get_completed_by_user(user)['data'][i]['completedAt']
                print(time)
                print(f"{user} has completed the kata {name_kata} at {time}")
                break
                #else:
                #print(f"{user} has NOT completed the kata {name_kata}")
                #return (user, kata_id, name_kata, False)

        return (user, kata_id, name_kata, time)
        
                # solo considera el primer id de kata porque pasa al return del else y acaba la función, ¿por qué? WHYYYYYYYYYY
    except: 
        print(f"Puede que {user} no tenga usuario")