from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def search():
    return render_template("index.html")

@app.route("/display", methods=['POST','GET'])
def display():
    word = request.form.get('search')
    print(word)
    return render_template("display.html", word=word)

if __name__ == '__main__':
    app.debug = True
    app.run()