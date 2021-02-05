import pandas as pd
import glob

# concat all data files to one csv
path = 'raw_files/*'
all_files = glob.glob(path)
all_files.sort()

li = []

for filename in all_files:
    print(filename)
    df = pd.read_csv(filename, index_col='tourney_date', header=0)
    li.append(df)

df = pd.concat(li, axis=0)
# df.sort_index(inplace=True)
df.sort_values(['tourney_date', 'match_num'], inplace=True)
df.to_csv('my_files/raw.csv', index=True, float_format='%g')
