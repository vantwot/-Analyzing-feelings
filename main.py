
"""
@author Valentina Salamanca 
"""
import pandas as pd
from textblob import TextBlob
import seaborn as sbn

df=pd.read_csv('nyt.csv')
print(df.head(10))