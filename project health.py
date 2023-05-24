# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:16:23 2023

@author: Melissa
"""

import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel("C:/Users\Admin\Desktop\disease and symptoms (1).xlsx")

# Clean all string columns
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].str.replace('"', '')
        df[column] = df[column].str.replace('{', '')
        df[column] = df[column].str.replace('}', '')
        df[column] = df[column].str.replace('[', '')
        df[column] = df[column].str.split(':').str.get(-1)

# Save the cleaned data to a new Excel file
df.to_excel("C:/Users\Admin\Desktop\cleaned_data.xlsx", index=False)
