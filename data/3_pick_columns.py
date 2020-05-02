import pandas as pd
import numpy as np


# concat
df = pd.read_csv('csv_files/full_data.csv', low_memory=False)

h2h = pd.read_csv('csv_files/h2h.csv')
wl = pd.read_csv('csv_files/wl.csv')
wl_last = pd.read_csv('csv_files/wl_last_x_matches.csv')
wl_tournament = pd.read_csv('csv_files/wl_this_tournament.csv')
wl_surface = pd.read_csv('csv_files/wl_this_surface.csv')

df = pd.concat([df, h2h[['H2HW', 'H2HL']], wl, wl_last, wl_tournament, wl_surface], axis=1)

# pick
df = df[[  # 'Court', 'Surface', 'Round', 'Best of',
         'Comment',
         'WRank', 'LRank',
         'B365W', 'B365L',  # 'PSW', 'PSL',
         'H2HW', 'H2HL',
         'P1W', 'P1L', 'P2W', 'P2L',
         'P1WX', 'P1LX', 'P2WX', 'P2LX',
         'P1WT', 'P1LT', 'P2WT', 'P2LT',
         'P1WS', 'P1LS', 'P2WS', 'P2LS'
         ]]

print('Full:', df.shape)

df = df[df.Comment == 'Completed']
del df['Comment']
print('Only completed:', df.shape)

df = df.dropna()
print('Drop na:', df.shape)

df = df.loc[df['B365W'] != df['B365L']]
print('No same odds:', df.shape)

print(df.columns)

df.to_csv('csv_files/selected_features.csv', index=False, float_format='%g')
