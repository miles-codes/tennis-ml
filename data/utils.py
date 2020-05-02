import pandas as pd
import numpy as np


def get_all_players(df):
    winners = df['Winner'].unique()
    losers = df['Loser'].unique()
    players = np.unique(np.append(winners, losers))
    return pd.DataFrame(players)


def players_results(df, row, x_matches=None, this_tournament=False, this_surface=False):
    p1 = row['Winner']
    p2 = row['Loser']
    date = row['Date']
    tournament = row['Tournament']
    surface = row['Surface']

    p1_matches = df.loc[
        ((df['Winner'] == p1) | (df['Loser'] == p1)) &
        (df['Date'] < date)
        ]
    p2_matches = df.loc[
        ((df['Winner'] == p2) | (df['Loser'] == p2)) &
        (df['Date'] < date)
        ]

    if x_matches:
        p1_matches = p1_matches.tail(x_matches)
        p2_matches = p2_matches.tail(x_matches)
    if this_tournament:
        p1_matches = p1_matches.loc[p1_matches['Tournament'] == tournament]
        p2_matches = p2_matches.loc[p2_matches['Tournament'] == tournament]
    if this_surface:
        p1_matches = p1_matches.loc[p1_matches['Surface'] == surface]
        p2_matches = p2_matches.loc[p2_matches['Surface'] == surface]

    p1_won = p1_matches[p1_matches.Winner == p1].shape[0]
    p1_loss = p1_matches.shape[0] - p1_won
    p2_won = p2_matches[p2_matches.Winner == p2].shape[0]
    p2_loss = p2_matches.shape[0] - p2_won

    return p1_won, p1_loss, p2_won, p2_loss


def h2h(df, row):
    winner = row['Winner']
    loser = row['Loser']
    date = row['Date']
    print(date)
    matches = df.loc[
        ((df['Winner'] == winner) & (df['Loser'] == loser)) |
        ((df['Winner'] == loser) & (df['Loser'] == winner))
        ]

    matches = matches.loc[matches['Date'] < date]

    won = matches[matches.Winner == winner].shape[0]
    loss = matches.shape[0] - won

    return won, loss


if __name__ == '__main__':
    data = pd.read_csv('csv_files/full_data.csv')
    r = data.iloc[[55408]]
    r = r.iloc[0]
    h2h(data, r)
    players_results(data, r, this_surface=True)
