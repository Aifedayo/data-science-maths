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

    
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_car_brand_name())