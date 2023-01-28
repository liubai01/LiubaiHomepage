from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Liubai01's homepage!</p>"


@app.route('/nav')
def nav():
    return render_template('nav.html', title='Recast Navigation')