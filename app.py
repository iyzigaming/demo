import requests
from flask import Flask
from flask import request
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)
@app.route('/demo',methods=['GET'])
def demo():
    ts = requests.get("http://germanydnsx11.com:8000/ZbLQXUxk/Es272827../89061",allow_redirects = True)
    return ts.text

if __name__ == '__main__':
    app.run()
