import os, sys
from flask import Flask, render_template, redirect, request, jsonify
import utils.json_reader as jr 
import time
import random
import json

# ----------------------
# $$$$$$$ CLASS INFO $$$$$$$$
# ----------------------

class Info:
    def __init__(self, restaurant, num_clients, location):
        self.restaurant = restaurant
        self.num_clients = num_clients
        self.location = location
        self.boss = "Wolfram"
        self.creation_date = "05/02/1465"
        
    def to_json(self):
        return jr.object_to_json(object=self)
    
    def __str__(self):
        return self.to_json()
        

# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")
def default():
    # Redirect
    #return redirect("http://aiconscience.ddns.net", code=302)
    return str(Info(2,3,4))

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get', methods=['GET'])
def get():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/restaurants', methods=['GET'])
def api_restaurants():
    """
    127.0.0.1:5072/api/restaurants?id=0
    """
    restaurant_id = None
    if 'id' in request.args:
        restaurant_id = int(request.args['id'])
    
    restaurant, num_clients = random.randint(1, 9999), random.randint(0, 60)
    location = [random.randint(-100, 100), random.randint(-100, 100)]
    new_restaurant = Info(restaurant=restaurant, 
                            num_clients=num_clients, 
                            location=location)
        
    return str(new_restaurant)

# ----------------------
# $$$$$$$ MAIN $$$$$$$$
# ----------------------

def main():
    
    print("STARTING PROCESS")
        
    INPUT_VALUE = ""
    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))  # This doesn't work in jupyter
    SETTING_PATH = CURRENT_PATH + os.sep + "settings.json"
    json_readed = jr.read_json_to_dict(json_fullpath=SETTING_PATH)
    
    SERVER_RUNNING = json_readed["server_running"]
    
    print(SETTING_PATH)
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. Please, allow it to run it.")
            
if __name__ == "__main__":
    main()
    