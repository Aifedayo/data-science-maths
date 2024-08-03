######################################
##           EXERCISE               ##
######################################

"""
Use this air bnb new york city data set and remove outliers using
percentile based on price per night for a given apartment/home.
You can use suitable upper and lower limits on percentile based
on your intuition. Your goal is to come up with new pandas dataframe
that doesn't have the outliers present in it.

"""
import os # For getting the source of the file
import pandas as pd # Data processing and reading csv files
import numpy as np # For linear algebra
import matplotlib.pyplot as plt # For visualization


df = pd.read_csv("/home/akeemlag/Downloads/archive-kaggle/AB_NYC_2019.csv")

# df.info()

# Visualize the data you have using .head()
print(df.head())

# Create a box plot to see the outliers using matplotlib


