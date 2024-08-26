import json
import joblib
import numpy as np
import pandas as pd

__name = None
__data_columns = None
__model = None


def get_car_brand_name():
    return __name

def load_saved_artifacts():
    print('loading saved artifacts...')
    global __name
    global __data_columns

    with open('../model/columns.json') as f:
        __data_columns = json.load(f)['data_columns']
        __name = __data_columns[7:16]

    global __model
    __model = joblib.load('../model/car_price_pred.pkl')


def get_estimated_price(
        name, year, km_driven, transmission, owner, seats, mileage, engine, seller_type, fuel):
    try:
        name_idx = __data_columns.index('name_'+ name)
        fuel_idx = __data_columns.index('fuel_'+ fuel)
        seller_type_idx = __data_columns.index('seller_type_'+seller_type)
    except:
        name_idx = -1
        fuel_idx = -1
        seller_type_idx = -1
    km_scaler = joblib.load('../model/km_scaler.pkl')
    km_driven_df = pd.DataFrame([[km_driven]], columns=['km_driven'])
    km_driven_scaled = km_scaler.transform(km_driven_df)[0][0]
    x = np.zeros(len(__data_columns))
    x[0] = year
    x[1] = km_driven_scaled
    x[2] = transmission
    x[3] = owner
    x[4] = seats
    x[5] = mileage
    x[6] = engine
    if name_idx >= 0:
        x[name_idx] = 1.0
    if fuel_idx >= 0:
        x[fuel_idx] = 1.0
    if seller_type_idx >= 0:
        x[seller_type_idx] = 1.0

    x_df = pd.DataFrame([x], columns=__data_columns)
    print(x_df)
    return __model.predict(x_df)[0]
    
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_car_brand_name())
    print(get_estimated_price(name='Maruti', year=13, km_driven=145500, owner=1, seats=5, mileage=22, engine=1000, seller_type='Individual', transmission=1, fuel='Petrol'))
    