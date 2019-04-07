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
    responseObject = json.loads(data)
    obs = responseObject["objects"]
    return obs

def parse_dict(d):
    for x in obs:
<<<<<<< HEAD
        print (x,"\n")
    return responseObject
=======
        print(x["properties"]['Name'],x["properties"]['enaio:objectId'],"\n")
    return d

>>>>>>> 25a8c133b2f495912ba0bd96bf2f00d973781a53
@app.route("/")
def search():
    return render_template("index.html")

@app.route("/display", methods=['POST','GET'])
def display():
    if request.method == 'POST':
        word = request.form['search']
        return render_template("display.html", word=word, data = build(word))
<<<<<<< HEAD
=======

@app.route('/app.js')
def script():
    return render_template('../static/js/script.js', d=d)

>>>>>>> 25a8c133b2f495912ba0bd96bf2f00d973781a53
if __name__ == '__main__':
    app.debug = True
    app.run()