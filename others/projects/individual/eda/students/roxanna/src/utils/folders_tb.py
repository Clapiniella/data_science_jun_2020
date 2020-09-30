

import pandas as pd
import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import time
import random
import json

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

def open_json(path):
    with open(path, "r+") as outfile:
        json = json.load(outfile)
        return json 