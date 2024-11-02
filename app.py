from flask import Flask, redirect, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/level/<string:level>')
def level(level):
    return render_template(f"{level}.html")

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response

def main():
    pass

if __name__ == "__main__":
    app.run(debug=True)