import pandas as pd
import numpy as np

df = pd.read_csv('history_data.csv')

group_cols = ['Background of Architect', 'Structure Type', 'Required Construction Materials', 'Characterization of Blueprints']
y_col = 'Is Completed Structure Impossible?'

# Get the number of unique categories for each column variable
n_rows = [df[col].nunique() for col in group_cols]
n_cols = df[y_col].nunique()

# Create an empty 2D numpy array to store the normalized counts
double_array = np.empty((sum(n_rows), n_cols))

# Fill in the array with the normalized counts for each category of each column variable
row_start = 0
for i, col in enumerate(group_cols):
    for j, cat in enumerate(df[col].unique()):
        counts = df[df[col] == cat][y_col].value_counts()
        norm_counts = counts / counts.sum()
        double_array[row_start+j, :] = norm_counts.values
    row_start += n_rows[i]

print(double_array)
