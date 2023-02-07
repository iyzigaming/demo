import requests
from flask import Flask
from flask import request
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)
@app.route('/demo',methods=['GET'])
def demo():
    long_url = ''
    url = 'http://germanydnsx11.com:8000/ZbLQXUxk/Es272827../89036'
    try:
        while True:
            long_url = requests.head(url).headers['location']
            print(long_url)
            url = long_url
    except:
        print(long_url)

if __name__ == '__main__':
    app.run()
