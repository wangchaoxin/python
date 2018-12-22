# 启动web FLASK_APP=flask/app.py flask run


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"