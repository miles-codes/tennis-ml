import pandas as pd


def favorite_won(row):
    return row['winner_rank'] < row['loser_rank']


def rank_ratio(row):
    if favorite_won(row):
        return row['loser_rank'] / row['winner_rank']
    else:
        return row['winner_rank'] / row['loser_rank']


def odds_ratio(row, c1, c2):
    return max(row[c1], row[c2]) / min(row[c1], row[c2])


def h2h_ratio(row):
    if favorite_won(row):
        return row['w_h2h'] - row['l_h2h']
    else:
        return row['l_h2h'] - row['w_h2h']


def is_favorite_seeded(row):
    if favorite_won(row):
        return pd.notnull(row['winner_seed'])
    else:
        return pd.notnull(row['loser_seed'])


def win_loss_ratio(row, c1, c2, c3, c4):
    wlw = row[c1] - row[c2]
    wll = row[c3] - row[c4]

    if favorite_won(row):
        return wlw - wll
    else:
        return wll - wlw


def serve_index(row):
    if favorite_won(row):
        try:
            return row['P1serve_index'] / row['P2serve_index']
        except ZeroDivisionError:
            return 1
    else:
        try:
            return row['P2serve_index'] / row['P1serve_index']
        except ZeroDivisionError:
            return 1


def non_favorite_entry(row):
    if favorite_won(row):
        return pd.isnull(row['loser_entry'])
    else:
        return pd.isnull(row['winner_entry'])


df = pd.read_csv('my_files/selected_features.csv')

df['RankRatio'] = df.apply(lambda row: rank_ratio(row), axis=1)
df['H2HRatio'] = df.apply(lambda row: h2h_ratio(row), axis=1)
df['ServeIndexRatio'] = df.apply(lambda row: serve_index(row), axis=1)
df['WLXRatio'] = df.apply(lambda row: win_loss_ratio(row, 'P1WX', 'P1LX', 'P2WX', 'P2LX'), axis=1)
df['WLTRatio'] = df.apply(lambda row: win_loss_ratio(row, 'P1WT', 'P1LT', 'P2WT', 'P2LT'), axis=1)
df['FavoriteSeeded'] = df.apply(lambda row: is_favorite_seeded(row), axis=1)
df['NonFavoriteEntry'] = df.apply(lambda row: non_favorite_entry(row), axis=1)
df['BestOf5'] = df['best_of'] == 5
df['output'] = df['winner_rank'] < df['loser_rank']

df = df.loc[(df['tourney_date'] >= 19901231)]

df.drop([
    'tourney_date',
    'surface', 'best_of', 'round',
    'winner_seed', 'winner_entry', 'winner_hand',
    'loser_seed', 'loser_entry', 'loser_hand',
    'winner_rank', 'loser_rank',
    'w_h2h', 'l_h2h',
    'P1WX', 'P1LX', 'P2WX', 'P2LX',
    'P1WT', 'P1LT', 'P2WT', 'P2LT',
    'P1serve_index', 'P2serve_index'
], axis=1, inplace=True)


print(df.shape)

df = df.dropna()

print(df.shape)
print((df.output == 1).sum())
print((df.output == 0).sum())

df.to_csv('my_files/ready.csv', index=False, float_format='%g')
