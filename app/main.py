from flask import Flask

app = Flask(__name__)

@app.route("/hello_pj")
def hello_world():
    return "<p>Hello, Universe!</p>";