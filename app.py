from flask import Flask, render_template, request, url_for
import urllib
import json
from http.client import HTTPSConnection
app = Flask(__name__)

headers = {
    'Authorization':"Basic YWRtaW46TGYwYll4dGo4UTdt",
    'X-ID-TENANT-NAME':"nyc093",
    'Content-Type':'application/json',
    'Accept':'application/json'
}

#This sets up the https connection
c = HTTPSConnection("yuuvis.io")

def build(word):
    host = "/api/dms/objects/search"
    payload = {
        "query": {
                "statement": "SELECT * FROM enaio:object where contains('%s')"%word,
                "skipCount": 0,
                "maxItems": 50
            }
    }
    json_load = json.dumps(payload)

    c.request('POST', host, json_load, headers = headers)
    #get the response back
    res = c.getresponse()
    # at this point you could check the status etc
    # this gets the page text
    data = res.read()
    print(data)

@app.route("/")
def search():
    return render_template("index.html")

@app.route("/display", methods=['POST','GET'])
def display():
    if request.method == 'POST':
        word = request.form['search']
        print(word)
        build(word)
        return render_template("display.html", word=word)

if __name__ == '__main__':
    app.debug = True
    app.run()