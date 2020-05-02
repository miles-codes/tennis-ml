import pandas as pd
import glob

# concat all excel files to one csv
path = 'excel_files/*.xl*'
all_files = glob.glob(path)
all_files.sort()

li = []

for filename in all_files:
    print(filename)
    df = pd.read_excel(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

# strip spaces from strings
df['Winner'] = df['Winner'].str.strip()
df['Loser'] = df['Loser'].str.strip()
df['Location'] = df['Location'].str.strip()
df['Tournament'] = df['Tournament'].str.strip()

# write data to csv
df.to_csv('csv_files/full_data.csv', index=False, float_format='%g')
df2 = pd.read_csv('csv_files/full_data.csv', skipinitialspace=True, low_memory=False)
df2.to_csv('csv_files/full_data.csv', index=False, float_format='%g')
