import pandas as pd
from sklearn import linear_model
import joblib

import pickle


df = pd.read_csv("/home/akeemlag/Downloads/homeprices-multiple.csv")
median_bedrooms = df.bedrooms.median()
df.bedrooms = df.bedrooms.fillna(median_bedrooms)


model = linear_model.LinearRegression()

X = df[["area", "bedrooms", "age"]]
y = df["price"]
model.fit(X, y)


with open("/home/akeemlag/Downloads/model/model_pickle", "wb") as file:
    pickle.dump(model, file)


with open("/home/akeemlag/Downloads/model/model_pickle", "rb") as file:
    model_pickle = pickle.load(file)


# Use model_pickle to make prediction
(model.predict([[3000, 3, 40]]))


"""
USING SKLEARN JOBLIB
"""
joblib.dump(model, '/home/akeemlag/Downloads/model/model_joblib')

model_joblib = joblib.load('/home/akeemlag/Downloads/model/model_joblib')

print(model_joblib.predict([[3000, 3, 40]]))
