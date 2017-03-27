from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world"


@app.route('/hello/<name>')
def hello(name):
    return "Hello, " + name


if __name__ == '__main__':
    app.run(debug=True)
