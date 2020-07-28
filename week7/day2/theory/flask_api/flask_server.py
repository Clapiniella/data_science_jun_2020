import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import time
import random
import json

# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")
def default():
    # Redirect
    #return redirect("http://aiconscience.ddns.net", code=302)
    #return str(request.args)
    return "I am the default function"

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get', methods=['GET'])
def get():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/test/', methods=['GET'])
def api_all():
    """
    127.0.0.1:6060/api/test/?id=0
    """
    restaurant_id = None
    if 'id' in request.args:
        restaurant_id = int(request.args['id'])
    
    if restaurant_id == 1:
        return "{'json': true}"
    elif restaurant_id == 99:
        return jsonify(col_1=[3, 2, 1, 0], col_2=['a', 'b', 'c', 'd'])
    else:
        return "This is a message of error" + "<br>" + "<br>" + str(request.args)

# ----------------------
# $$$$$$$ MAIN $$$$$$$$
# ----------------------

def main():
    
    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(__file__) + "\\settings.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
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
    