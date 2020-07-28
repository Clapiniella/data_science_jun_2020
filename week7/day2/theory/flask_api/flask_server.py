import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json

html = """<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Página de prueba</title>
</head>
<body>
<div id="main" class="full-width">
    <h1>El título de la página</h1>
    <p>Este es el primer párrafo</p>
    <p>Este es el segundo párrafo</p>
    <div id="innerDiv">
        <div class="links">
            <a href="https://pagina1.xyz/">Enlace 1</a>
            <a href="https://pagina2.xyz/">Enlace 2</a>
        </div>
        <div class="right">
            <div class="links">
                <a href="https://pagina3.xyz/">Enlace 3</a>
                <a href="https://pagina4.xyz/">Enlace 4</a>
            </div>
        </div>
    </div>
    <div id="footer">
        <!-- El footer -->
        <p>Este párrafo está en el footer</p>
        <div class="links footer-links">
            <a href="https://pagina5.xyz/">Enlace 5</a>
        </div>
    </div>
</div>
</body>
</html>"""

# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/")  # Default path
def default():
    # Redirect
    #return redirect("http://aiconscience.ddns.net", code=302)
    #return str(request.args)
    return html

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get', methods=['GET'])
def get():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['id']
    return request.args

# A route to return all of the available entries in our catalog.
@app.route('/api/test/', methods=['GET'])
def api_all():
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