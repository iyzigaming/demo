import requests
from flask import Flask
from flask import request
from flask_cors import CORS
import re
app = Flask(__name__)
CORS(app)
#https://tulipbettv44.com
#https://monotv100.live/
#https://levant2.tv
@app.route('/getm3u8',methods=['GET'])
def getm3u8():
    source = request.args.get("source")
    headers = {
'accept': '*/*',
'accept-language': 'tr-TR,tr;q=0.9',
'origin': 'https://kalebettv29.com',
'referer': 'https://kalebettv29.com/',
'sec-ch-ua': '"Opera";v="95", "Chromium";v="109", "Not;A=Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0'
    }
    ts = requests.get(source, headers=headers)
    tsal = ts.text
    tsal = tsal.replace("https://","https://testyayin.herokuapp.com/getcss?source=https://")
    if "mediaplaylist.json" in tsal:
        source2 = source.replace("https://","").split("/")
        source2 = source[2].replace(".m3u8","")
        source = source.replace("https://","").split("/")
        tsal = tsal.replace(source2+"/1","https://testyayin.herokuapp.com/getcss?source=https://"+source[0]+"/"+source[1])
    #tsal = tsal.split('"')
    #host = tsal[2].replace("\n","")
    return tsal
    
    
@app.route('/getcss',methods=['GET'])
def getcss():
    source = request.args.get("source")
    headers = {
'accept': '*/*',
'accept-language': 'tr-TR,tr;q=0.9',
'origin': 'https://kalebettv29.com',
'referer': 'https://kalebettv29.com/',
'sec-ch-ua': '"Opera";v="95", "Chromium";v="109", "Not;A=Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0'
    }
    host = source.replace("https://","").split("/")
    host = "https://"+host[0]+"/"+host[1]+"/"
    host = host.replace("https:// ","https://")
    ts = requests.get(source, headers=headers)
    ts = ts.text.replace(",\n",",\n"+"https://testyayin.herokuapp.com/getjpeg?source="+host)
    return ts  


@app.route('/getjpeg',methods=['GET'])
def getjpeg():
    source = request.args.get("source")
    headers = {
'accept': '*/*',
'accept-language': 'tr-TR,tr;q=0.9',
'origin': 'https://kalebettv29.com',
'referer': 'https://kalebettv29.com/',
'sec-ch-ua': '"Opera";v="95", "Chromium";v="109", "Not;A=Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0'
    }
    ts = requests.get(source, headers=headers)
    ts = ts.content
    return ts      

if __name__ == '__main__':
    app.run()

