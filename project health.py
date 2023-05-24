# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:16:23 2023

@author: Melissa
"""

import pandas as pd
import json

#df  = pd.read_csv('C:/Users/Melissa/OneDrive - Avans Hogeschool/Documents/Utrecht/datasets/flights.csv')

df = pd.read_excel('C:/Users/Melissa/OneDrive - Avans Hogeschool/Desktop/disease and symptoms.xlsx')

#get the data ready 
#[{"symptoms":"Anxiety and nervousness"}

#df['Address'] = df['Address'].str.split(',').str.get(-1)
df['symptoms'] = df['symptoms'].str.replace('"',"")
df['symptoms'] = df['symptoms'].str.replace('{',"")
df['symptoms'] = df['symptoms'].str.replace('}',"")
df['symptoms'] = df['symptoms'].str.replace('[',"")

df['symptoms'] = df['symptoms'].str.split(':').str.get(-1)