from flask import Flask

## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask web.This should be fun."

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__ == "__main__":
    app.run(debug=True)