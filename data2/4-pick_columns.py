import pandas as pd
import numpy as np
# concat
df = pd.read_csv('my_files/raw.csv', low_memory=False)

h2h = pd.read_csv('my_files/raw_h2h.csv')
wl_last = pd.read_csv('my_files/wl_last_15_matches.csv')
wl_tournament = pd.read_csv('my_files/wl_this_tournament.csv')
serve_index = pd.read_csv('my_files/serve_index.csv')

df = pd.concat([df, h2h[['w_h2h', 'l_h2h']], wl_last, wl_tournament, serve_index], axis=1)

# pick
df = df[[
    'tourney_date', 'score',
    'surface', 'best_of', 'round',
    'winner_seed', 'winner_entry', 'winner_hand',
    'loser_seed', 'loser_entry', 'loser_hand',
    'winner_rank', 'loser_rank',
    'w_h2h', 'l_h2h',
    'P1WX', 'P1LX', 'P2WX', 'P2LX',
    'P1WT', 'P1LT', 'P2WT', 'P2LT',
    'P1serve_index', 'P2serve_index'
]]

print('Full:', df.shape)

df = df[df["score"].str.contains('RET') == False]
df = df[df["score"].str.contains('W/O') == False]
del df['score']
print('Only completed:', df.shape)

# df = df.dropna()
# print('Drop na:', df.shape)

# df = df.loc[df['B365W'] != df['B365L']]
# print('No same odds:', df.shape)

# print(df.columns)

df.to_csv('my_files/selected_features.csv', index=False, float_format='%g')
