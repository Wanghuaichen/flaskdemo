from flask import Flask
fdsafdsa
app = Flask(__name__)

@app.route('/')
def hello():
    msg = "Hello wh!"
    return 'Hello World'
