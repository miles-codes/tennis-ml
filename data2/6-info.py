import pandas as pd

df = pd.read_csv('my_files/ready.csv')
print((df.output == 1).sum() / df.shape[0])

df_test = df.loc[(df['BestOf5'] == 1)]
print(df_test.shape)
print((df_test.output == 1).sum() / df_test.shape[0])
