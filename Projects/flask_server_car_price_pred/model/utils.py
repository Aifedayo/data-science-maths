# util function for data cleaning
from datetime import datetime

def find_outliers(col_name, df):
    # Use quantile to reassign outliers
    q1 = df[col_name].quantile(0.25)
    q3 = df[col_name].quantile(0.75)
    iqr = q3 - q1
    upper_limit = q3 + 1.5*iqr
    lower_limit = q1 - 1.5*iqr
    outliers = df[(df[col_name] > upper_limit)] | (df[col_name < lower_limit])
    print(f'There are {outliers.shape[0]} outliers')
    return outliers
