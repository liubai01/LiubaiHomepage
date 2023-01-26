from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Liubai01's homepage!</p>"


@app.route("/nav")
def nav():
    return "<p>Recast Navigation Homepage!</p>"