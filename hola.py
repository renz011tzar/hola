import pandas as pd
import numpy as np

from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('history_data.csv')
# Get the column names of the DataFrame
column_names = df.columns.tolist()

# Print the column names
print(column_names)

# Create a countplot between two columns
sns.countplot(data=df, x='Is Completed Structure Impossible?', hue='Background of Architect')

# Show the plot
plt.show()

group_cols = ['Background of Architect', 'Structure Type', 
              'Required Construction Materials', 'Characterization of Blueprints']
table = []

group_cols = ['Background of Architect', 'Structure Type', 
              'Required Construction Materials', 'Characterization of Blueprints']
table = []

for col in group_cols:
    counts = df.groupby(col)['Is Completed Structure Impossible?'].value_counts()
    normalized_counts = counts.groupby(level=0).apply(lambda x: x / float(x.sum()))
    for group in normalized_counts.index.levels[0]:
        if (group, 0) not in normalized_counts[group].index:
            normalized_counts[group] = normalized_counts[group].append(pd.Series(0, index=[(group, 0)]))
        if (group, 1) not in normalized_counts[group].index:
            normalized_counts[group] = normalized_counts[group].append(pd.Series(0, index=[(group, 1)]))
    normalized_array = normalized_counts.values
    table.append(normalized_array)

for i in range(len(table)):
    print(f"Table {i+1}: {group_cols[i]}")
    for row in table[i]:
         print(row)
    print("\n")
