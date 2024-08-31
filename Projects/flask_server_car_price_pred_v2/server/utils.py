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
    _artifacts['model_rfr'] = joblib.load('artifacts/model_rfr.pkl')
    _artifacts['model_xgb'] = joblib.load('artifacts/model_xgb.pkl')

if __name__ == '__main__':
    load_artifacts()
    print(_artifacts['colors_columns'])
    print(get_exact_value(_artifacts['colors_columns'], 'Colors', 'Redui'))
    print(_artifacts['fuels'])
    print(_artifacts['data_columns'])
