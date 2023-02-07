import requests
from flask import Flask
from flask import request
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)
@app.route('/demo',methods=['GET'])
def demo():
    r = requests.head("http://germanydnsx11.com:8000/ZbLQXUxk/Es272827../89036", allow_redirects=False)
    r.raise_for_status()
    if 300 < r.status_code < 400:
        url = r.headers.get('Location', url)

    return url

if __name__ == '__main__':
    app.run()
