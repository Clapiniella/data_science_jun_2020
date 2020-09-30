
### nog aanpassen want dit is van het groepsproject corona!!

import pandas as pd
import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import time
import random
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)



def dfjson(df, year):
    if year == 2015:
        df.to_json("C:\\Users\\Roxan\\OneDrive\\Documentos\\Project_world_happiness\\Project_world_happiness\\Resources\\data_2015.json") #converting to Json mean
        return "File data_2015.json has been loaded"
    elif year == 2016:
        df.to_json("C:\\Users\\Roxan\\OneDrive\\Documentos\\Project_world_happiness\\Project_world_happiness\\Resources\\data_2016.json") #converting to Json mean
        return "File data_2016.json has been loaded"
    elif year == 2017:
        df.to_json("C:\\Users\\Roxan\\OneDrive\\Documentos\\Project_world_happiness\\Project_world_happiness\\Resources\\data_2017.json") #converting to Json mean
        return "File data_2017.json has been loaded"
    elif year == 2018:
        df.to_json("C:\\Users\\Roxan\\OneDrive\\Documentos\\Project_world_happiness\\Project_world_happiness\\Resources\\data_2018.json") #converting to Json mean
        return "File data_2018.json has been loaded"
    elif year == 2019:
        df.to_json("C:\\Users\\Roxan\\OneDrive\\Documentos\\Project_world_happiness\\Project_world_happiness\\Resources\\data_2019.json") #converting to Json mean
        return "File data_2019.json has been loaded"
    elif year == "All":
        df.to_json("C:\\Users\\Roxan\\OneDrive\\Documentos\\Project_world_happiness\\Project_world_happiness\\Resources\\data_all_years.json") #converting to Json mean
        return "File data_all_years.json has been loaded"

