import pandas as pd
pd.set_option('display.max_columns', 15)

df = pd.read_excel('hospital.xlsx')

print(df.head())

ids = df['UNIQUE HOSPITAL ID'].values.tolist()
names = df['HOSPITAL NAME'].values.tolist()
address = df['ADDRESS'].values.tolist()