from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def search():
    return render_template("search.html")

@app.route("/display", methods=['POST','GET'])
def display():
    #first = request.form.get('firstname')
    last = request.form.get('lastname')
    return render_template("display.html", first="first", last=last)
    
if __name__ == '__main__':
    app.debug = True
    app.run()