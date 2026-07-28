from scripts.load import read_dataframe

df = read_dataframe("raw", "sales")

print(df.head())

print(df.shape)