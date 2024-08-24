from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = (request.form['location'])
    BHK = float(request.form['BHK'])
    bath = float(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_prices(location, total_sqft, BHK, bath)
    })
    return response



if __name__ == '__main__':
    print("Starting Python Flask Server for Home Price Prediction")
    app.run()