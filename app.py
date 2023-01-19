# To run app in Powershell
## set FLASK_APP=app.py
## $env:FLASK_APP = "app.py"
## flask run

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world"


if __name__ == "__main__":
    app.run()
