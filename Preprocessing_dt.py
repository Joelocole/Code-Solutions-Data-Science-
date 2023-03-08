import pandas as pd

# import
path = r"..\data\outputs\output_long.csv"

df = pd.read_csv(path)


# COLUMNS STANDARDISATION

# 1 solution
df.columns = [char.replace(".", "_").replace(" ", "_") for char in [col_name.upper() for col_name in df.columns]]

# 2 solution
df.rename(columns=lambda x: x.replace(".", "_").replace(" ", "_"), inplace=True)

print(f"b dataframe shape: {df.shape}")
print(f"b standardised columns: {df.columns}")
