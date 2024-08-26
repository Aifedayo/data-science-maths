from flask import Flask, jsonify, request
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_home_page():
    return 'Hello World!'



if __name__ == '__main__':
    print('Starting Python Flask Serve for Car Price Prediction...')
    app.run()
