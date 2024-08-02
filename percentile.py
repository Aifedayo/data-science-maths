import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Akeem", "Zainab", "Abdullah", "Abdulmalik", "Abdurrahman", "Abdurraheem"],
    "Score": [56, 58, 64, 69, 70, 87]
})

df.describe()
print(df.Score.quantile(.40, interpolation="lower"))

print(df[df.Score > df.Score.quantile(0.9)])

## Create a new dataframe with no outlier
df_no_outlier = df[df.Score <= df.Score.quantile(.90)]
print(df_no_outlier)

