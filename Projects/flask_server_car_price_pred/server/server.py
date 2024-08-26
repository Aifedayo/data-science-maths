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
    name = request.form['name']
    year = int(request.form['year'])
    km_driven = int(request.form['km_driven'])
    transmission = (request.form['transmission'])
    owner = (request.form['owner'])
    seats = (request.form['seats'])
    mileage = (request.form['mileage'])
    engine = int(request.form['engine'])
    seller_type = request.form['seller_type']
    fuel = request.form['fuel']

    response = jsonify({
        'estimated_price': float(util.get_estimated_price(
            name, year, km_driven, transmission, owner, seats, mileage,
            engine, seller_type, fuel))
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting Python Flask Serve for Car Price Prediction...')
    util.load_saved_artifacts()
    app.run()

