from flask import Flask, make_response, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def form():
    return """
        <html>
            <body style="background-color: #81bdff;" >
                <h1>Get the shape of your data:</h1>
                <p> Enter your data in <b>CSV</b> or <b>JSON</b> format and you'll get the number of columns and rows it has. 
                Since you have to have that file in your computer, in order to upload it, this program
                won't save the file again.
                </p>
                <form action="/shape" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/shape', methods=["POST"])
def get_shape():
    request_file = request.files['data_file']

    if not request_file:
        return "No file"

    if ".csv" in str(request_file)
        data = pd.read_csv(request_file)
        return """
        <html>
            <body style="background-color: #d1bfff;">
                <h2>This CSV has {a} columns and {b} rows</h2>
            </body>
        </html>
    """.format(a = data.shape[0], b = data.shape[1])

    elif ".json" in str(request_file):
        data = pd.read_json(request_file.read())
        return """
        <html>
            <body style="background-color: #d1bfff;">
                <h2>This JSON has {a} columns and {b} rows</h2>
            </body>
        </html>
    """.format(a = data.shape[0], b = data.shape[1])


app.run(host='0.0.0.0',port=7770,debug=True)