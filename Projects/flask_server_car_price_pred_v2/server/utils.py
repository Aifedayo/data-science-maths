import json
import joblib
import numpy as np
import pandas as pd

# global variables
__manufacturers = None
__models = None
__categories = None
__colors = None
__fuels = None
__gear_boxes = None
__drive_wheels = None

# Variable for models
__model_xgb = None
__model_rfr = None


# json columns
__data_columns = None
__manufacturers_to_models_columns = None
__manufacturers_columns = None
__models_columns = None
__categories_columns = None
__colors_columns = None
__gear_box_types_columns = None
__fuel_types_columns = None
__drive_wheels_columns = None


def get_exact_value(column, name, key):
    value = column[name].get(key, 0)
    return value

def load_artifacts():
    global __manufacturers_columns
    global __models_columns
    global __categories_columns
    global __colors_columns
    global __fuel_types_columns
    global __gear_box_types_columns
    global __drive_wheels_columns

    global __manufacturers
    global __models
    global __categories
    global __colors
    global __fuels
    global __drive_wheels
    global __gear_boxes
    
    with open('artifacts/Manufacturer.json') as f:
        __manufacturers_columns = json.load(f)
        __manufacturers = list(__manufacturers_columns['Manufacturers'].keys())
    
    with open('artifacts/Model.json') as f:
        __models_columns = json.load(f)
        __models = list(__models_columns['Models'].keys())
    
    with open('artifacts/Category.json') as f:
        __categories_columns = json.load(f)
        __categories = list(__categories_columns['Categorys'].keys())
    
    with open('artifacts/Color.json') as f:
        __colors_columns = json.load(f)
        __colors = list(__colors_columns['Colors'].keys())
    
    with open('artifacts/Gear_box_type.json') as f:
        __gear_box_types_columns = json.load(f)
        __categories = list(__gear_box_types_columns['Gear_box_types'].keys())
    
    with open('artifacts/Fuel_type.json') as f:
        __fuel_types_columns = json.load(f)
        __fuels = list(__fuel_types_columns['Fuel_types'].keys())
    
    with open('artifacts/Drive_wheels.json') as f:
        __drive_wheels_columns = json.load(f)
        __drive_wheels = list(__drive_wheels_columns['Drive_wheelss'].keys())

    global __manufacturers_to_models_columns
    global __data_columns

    with open('artifacts/columns.json') as f:
        __data_columns = json.load(f)['data_columns']
    with open('artifacts/manufactures_to_models.json') as f:
        __manufacturers_to_models_columns = json.load(f)


    global __model_rfr
    global __model_xgb

    __model_rfr = joblib.load('artifacts/model_rfr.pkl')
    __model_xgb = joblib.load('artifacts/model_xgb.pkl')


if __name__ == '__main__':
    load_artifacts()
    print(__colors_columns)
    print(get_exact_value(__colors_columns, 'Colors', 'Redui'))
    print(__fuels)
    print(__data_columns)
