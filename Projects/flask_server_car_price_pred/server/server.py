from flask import Flask, jsonify, request
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/car_brand')
def get_car_brand_name():
    response = jsonify({
        'car_brands': util.get_car_brand_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_car_price', methods=['POST'])
def predict_car_price():
    


if __name__ == '__main__':
    print('Starting Python Flask Serve for Car Price Prediction...')
    util.load_saved_artifacts()
    app.run()
