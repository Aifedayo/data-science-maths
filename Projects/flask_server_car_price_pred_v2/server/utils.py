import json
import joblib
import numpy as np
import pandas as pd

# Global variables
_artifacts = {
    "manufacturers": None,
    "models": None,
    "categories": None,
    "colors": None,
    "fuels": None,
    "gear_boxes": None,
    "drive_wheels": None,
    "manufacturers_columns": None,
    "models_columns": None,
    "categories_columns": None,
    "colors_columns": None,
    "fuel_types_columns": None,
    "gear_box_types_columns": None,
    "drive_wheels_columns": None,
    "data_columns": None,
    "manufacturers_to_models_columns": None,
    'scaler': None,
    "model_xgb": None,
    "model_rfr": None
}

def get_exact_value(column, name, key):
    """Returns the exact value from a nested dictionary, defaults to 0 if the key is not found."""
    return column.get(name, {}).get(key, 0)

def load_json_artifact(filepath):
    """Loads a JSON file and returns its contents."""
    with open(filepath, 'r') as file:
        return json.load(file)

def load_artifacts():
    """Loads all necessary artifacts for the model and assigns them to global variables."""
    global _artifacts
    
    # Load JSON artifacts
    _artifacts['manufacturers_columns'] = load_json_artifact('artifacts/Manufacturer.json')
    _artifacts['models_columns'] = load_json_artifact('artifacts/Model.json')
    _artifacts['categories_columns'] = load_json_artifact('artifacts/Category.json')
    _artifacts['colors_columns'] = load_json_artifact('artifacts/Color.json')
    _artifacts['gear_box_types_columns'] = load_json_artifact('artifacts/Gear_box_type.json')
    _artifacts['fuel_types_columns'] = load_json_artifact('artifacts/Fuel_type.json')
    _artifacts['drive_wheels_columns'] = load_json_artifact('artifacts/Drive_wheels.json')
    _artifacts['manufacturers_to_models_columns'] = load_json_artifact('artifacts/manufactures_to_models.json')
    _artifacts['data_columns'] = load_json_artifact('artifacts/columns.json')['data_columns']

    # Extract specific keys
    _artifacts['manufacturers'] = list(_artifacts['manufacturers_columns']['Manufacturers'].keys())
    _artifacts['models'] = list(_artifacts['models_columns']['Models'].keys())
    _artifacts['categories'] = list(_artifacts['categories_columns']['Categorys'].keys())
    _artifacts['colors'] = list(_artifacts['colors_columns']['Colors'].keys())
    _artifacts['gear_boxes'] = list(_artifacts['gear_box_types_columns']['Gear_box_types'].keys())
    _artifacts['fuels'] = list(_artifacts['fuel_types_columns']['Fuel_types'].keys())
    _artifacts['drive_wheels'] = list(_artifacts['drive_wheels_columns']['Drive_wheelss'].keys())

    # Load model artifacts
    _artifacts['scaler'] = joblib.load('artifacts/mileage_scaler.pkl')
    _artifacts['model_rfr'] = joblib.load('artifacts/model_rfr.pkl')
    _artifacts['model_xgb'] = joblib.load('artifacts/model_xgb.pkl')



def predict_used_car_price(**kwargs):
    """Util function to predict the price of a used car."""
    
    x = np.zeros(len(_artifacts['data_columns']))
    
    for key, value in kwargs.items():
        # value = value.title()
        
        if key == 'levy':
            x[0] = value
        
        elif key == 'manufacturer':
            x[1] = get_exact_value(_artifacts['manufacturers_columns'], 'Manufacturers', value)
        
        elif key == 'model':
            x[2] = get_exact_value(_artifacts['models_columns'], 'Models', value)
        
        elif key == 'prod_year':
            x[3] = value
        
        elif key == 'category':
            x[4] = get_exact_value(_artifacts['categories_columns'], 'Categorys', value)
        
        elif key == 'interior':
            x[5] = 1 if value == 'Leather' else 0
        
        elif key == 'fuel_type':
            x[6] = get_exact_value(_artifacts['fuel_types_columns'], 'Fuel_types', value)
        
        elif key == 'engine_volume':
            x[7] = value
        
        elif key == 'mileage':
            mileage_df = pd.DataFrame([[value]], columns=['Mileage'])
            x[8] = _artifacts['scaler'].transform(mileage_df)[0][0]
        
        elif key == 'cylinder':
            x[9] = value
        
        elif key == 'gear_box_type':
            x[10] = get_exact_value(_artifacts['gear_box_types_columns'], 'Gear_box_types', value)
        
        elif key == 'drive_wheel':
            x[11] = get_exact_value(_artifacts['drive_wheels_columns'], 'Drive_wheelss', value)
        
        elif key == 'color':
            x[12] = get_exact_value(_artifacts['colors_columns'], 'Colors', value)
        
        elif key == 'airbag':
            x[13] = value
    
    x_df = pd.DataFrame([x], columns=_artifacts['data_columns'])

    print('Predicting with XGBoostRegressor...')
    print(_artifacts['model_xgb'].predict(x_df)[0])
    print()
    print('Predicting with RandomForestRegressor...')
    print(_artifacts['model_rfr'].predict(x_df)[0])

if __name__ == '__main__':
    load_artifacts()
    # print(_artifacts['colors_columns'])
    # print(get_exact_value(_artifacts['colors_columns'], 'Colors', 'Redui'))
    # print(_artifacts['fuels'])
    # print(_artifacts['data_columns'])
    print(predict_used_car_price(
        levy=1234,
        manufacturer='HonDa', 
        model='Civic', 
        category='sedan',
        prod_year=2018, 
        fuel_type='Petrol', 
        color='Yellow', 
        engine_volume=3.5, 
        drive_wheel='4x4', 
        airbag=10, 
        cylinder=12, 
        mileage=145000, 
        interior='Leather')
    )
