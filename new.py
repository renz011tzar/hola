import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('history_data.csv')
column_names = df.columns.tolist()
print(column_names)


group_cols = ['Background of Architect', 'Structure Type', 
              'Required Construction Materials', 'Characterization of Blueprints']

for col in group_cols:
     table_1=pd.crosstab(df[col], df['Is Completed Structure Impossible?'])
     prop_table_1=pd.crosstab(df[col], df['Is Completed Structure Impossible?'], normalize='index')
     print(prop_table_1)


