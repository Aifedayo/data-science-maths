# util function for data cleaning
from datetime import datetime

def find_outliers(col_name, df):
    # Use quantile to reassign outliers
    q1 = df[col_name].quantile(0.25)
    q3 = df[col_name].quantile(0.75)
    iqr = q3 - q1
    upper_limit = q3 + 1.5*iqr
    lower_limit = 1.5*iqr - q1
    print(f'upper_limit: ', {upper_limit})
    print(f'lower_limit: ', {lower_limit})
    outliers = df[(df[col_name] > upper_limit) | (df[col_name] < lower_limit)]
    print(f'There are {outliers.shape[0]} outliers')
    return outliers


def clean_owner_col(owner):
    owner_map = {
        'First Owner': 1, 
        'Second Owner': 2,
        'Third Owner': 3,
        'Fourth & Above Owner': 4, 
        'Test Drive Car': 0
    }
    return owner_map.get(owner, -999)


def clean_year_owned(col_name, df):
    year_now = datetime.now().year
    df.col_name = df.col_name.apply(lambda x: year_now - x)
    return df.col_name.info()


def display_outliers(df, plt):
    numerical_cols = df.select_dtypes(include=['int', 'float']).columns  
    print((numerical_cols))  
    fig, axs = plt.subplots(3, 2, figsize=(15,10))
    for idx, col in enumerate(numerical_cols):
        if  len(df[col].unique()) > 10:
            mat1 = idx % 3
            mat2 = idx % 2
            df[col].plot(kind='box', ax=axs[mat1, mat2])
            plt.title(f'Box plot of {col}')
            plt.xlabel(col)
            plt.ylabel('Values')
        else:
            continue
    