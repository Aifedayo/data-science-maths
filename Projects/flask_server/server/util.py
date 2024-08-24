import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None


def get_estimated_prices(location, total_sqft, BHK, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = BHK
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    
    x_df = pd.DataFrame([x], columns=__data_columns)
    return round(__model.predict(x_df)[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("../artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("../artifacts/house-pricing-model", "rb") as f:
        __model = pickle.load(f)

    print('Loading saved artifacts...done!')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_prices('1st phase JP Nagar', 1000, 3, 3))
    print(get_estimated_prices('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_prices('Kalhalli', 1000, 2, 2))
    print(get_estimated_prices('Ejipura', 1000, 2, 2))
