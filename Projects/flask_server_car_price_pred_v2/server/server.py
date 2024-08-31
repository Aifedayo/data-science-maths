from flask import Flask, jsonify, request
from flask_cors import CORS

import utils

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello there'



if __name__ == '__main__':
    print('Starting flask server for used car price prediction...')
    app.run()
