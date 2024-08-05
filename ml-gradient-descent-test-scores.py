import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math


# Predict using sklearn
def predict_using_sklearn(df):
    df = pd.read_csv(df)
    reg = LinearRegression()
    reg.fit(df[["math"]], df.cs)

    return reg.coef_, reg.intercept_


def using_gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.001

    cost_previous = 0

    for i in range(iterations):
        y_predicted = (m_curr * x) + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n) * sum(x*(y-y_predicted))
        bd = -(2/n) * sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print("m: {}, b: {}, cost: {}, iterations: {}".format(m_curr, b_curr, cost, i))

    return m_curr, b_curr

if __name__ == "__main__":
    m_sklearn, b_sklearn = predict_using_sklearn("/home/akeemlag/Downloads/test_scores.csv")
    print(m_sklearn, b_sklearn)

    df = pd.read_csv("/home/akeemlag/Downloads/test_scores.csv")
    x = np.array(df.math)
    y = np.array(df.cs)

    m_curr, b_curr = using_gradient_descent(x,y)
    print(m_curr, b_curr)
