import pandas as pd

csv_file_path = 'iris.csv'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type']
df = pd.read_csv(csv_file_path, header=None, names=column_names)
df = df.drop(1)

# Print the DataFrame with custom index starting from 0
print("sepal_length  sepal_width  petal_length  petal_width    species_type")
for idx, row in df.reset_index(drop=True).iterrows():
    print(f"{idx:<5}{row['sepal_length']:<13}{row['sepal_width']:<13}{row['petal_length']:<13}{row['petal_width']:<13}{row['species_type']}")