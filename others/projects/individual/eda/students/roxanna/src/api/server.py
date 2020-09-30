
### Api to return the dataframe in Json format of all years combined when token_id is put in and returning only dataframe of specific year when year is provided as argument.


import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import time
import random
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)
print(sys.path)
from src.utils.folders_tb import open_json

app = Flask(__name__)


@app.route("/")
def default():
    return "Hi, there :)"


@app.route('/get/Data', methods=['GET'])
def get():
    token_id_number = None
    year_id = None
    S =  "Y7291372H" 
    path = root_path + "\\Resources\\data_all_years.json"
    path_2015 = root_path + "\\Resources\\data_2015.json"
    path_2016 = root_path + "\\Resources\\data_2016.json" 
    path_2017 = root_path + "\\Resources\\data_2017.json"
    path_2018 = root_path + "\\Resources\\data_2018.json"
    path_2019 = root_path + "\\Resources\\data_2019.json"
     
    #direction to where json is saved.    
    
    if 'token_id' in request.args:
        token_id_number = str(request.args['token_id'])
    
        if token_id_number == S:

            return open_json(path)
            #Have to add the information that is assigned to our group 

    if 'year' in request.args:
        year_id = str(request.args['year'])
        if year_id == '2015':
            return open_json(path_2015)
        elif year_id == '2016':
            return open_json(path_2016)
        elif year_id == '2017':
            return open_json(path_2017)
        elif year_id == '2018':
            return open_json(path_2018)
        elif year_id == '2019':
            return open_json(path_2019)



    else:
         return "This is a message of error" + "<br>" + "<br>" + str(request.args)


def main():
    
    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    

    settings_file = os.path.dirname(__file__) + "\\settings.json"
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)

    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()