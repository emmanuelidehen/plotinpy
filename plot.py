#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 07:37:51 2020

@author: emmanuelidehen
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({'Rainy':[29,28,32,35,36,12,18,30,45,55, 32,32,32,32,32], 'City':['City_A']*5 + ['City_B']*5 + ['City_C']*5})
print(df)
print ("............................................")
print(np.mean(df[df['City'] == 'City_A']['Rainy']))

print(np.mean(df[df['City'] == 'City_B']['Rainy']))

print(np.mean(df[df['City'] == 'City_C']['Rainy']))
print ("............................................")
print(np.std(df[df['City'] == 'City_A']['Rainy']))

print(np.std(df[df['City'] == 'City_B']['Rainy']))

print(np.std(df[df['City'] == 'City_C']['Rainy']))
print ("............................................")
sns.lineplot(y='Rainy', x='City', data=df)
plt.show()