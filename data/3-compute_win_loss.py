import datetime
import pandas as pd
import numpy as np

def players_results(df, row, x_matches=None, this_tournament=False, this_surface=False):
    p1 = row['winner_id']
    p2 = row['loser_id']
    date = row['tourney_date']
    tournament = row['tourney_name']
    surface = row['surface']

    p1_matches = df.loc[
        ((df['winner_id'] == p1) | (df['loser_id'] == p1)) &
        (df['tourney_date'] <= date)
        ]
    p1_matches = p1_matches.drop(
        p1_matches[(p1_matches['tourney_date'] == date) & (p1_matches['match_num'] >= row['match_num'])].index
    )
    p1_matches.reset_index(inplace=True)

    p2_matches = df.loc[
        ((df['winner_id'] == p2) | (df['loser_id'] == p2)) &
        (df['tourney_date'] <= date)
        ]
    p2_matches = p2_matches.drop(
        p2_matches[(p2_matches['tourney_date'] == date) & (p2_matches['match_num'] >= row['match_num'])].index
    )
    p2_matches.reset_index(inplace=True)

    if x_matches:
        p1_matches = p1_matches.tail(x_matches)
        p2_matches = p2_matches.tail(x_matches)
    if this_tournament:
        p1_matches = p1_matches.loc[p1_matches['tourney_name'] == tournament]
        p2_matches = p2_matches.loc[p2_matches['tourney_name'] == tournament]
    if this_surface:
        p1_matches = p1_matches.loc[p1_matches['surface'] == surface]
        p2_matches = p2_matches.loc[p2_matches['surface'] == surface]

    p1_won = p1_matches[p1_matches.winner_id == p1].shape[0]
    p1_loss = p1_matches.shape[0] - p1_won
    p2_won = p2_matches[p2_matches.winner_id == p2].shape[0]
    p2_loss = p2_matches.shape[0] - p2_won

    return p1_won, p1_loss, p2_won, p2_loss


def last_match_stats(df, row):
    p1 = row['winner_id']
    p2 = row['loser_id']
    date = row['tourney_date']
    p1_matches = df.loc[
        ((df['winner_id'] == p1) | (df['loser_id'] == p1)) &
        (df['tourney_date'] <= date)
        ]
    p1_matches = p1_matches.drop(
        p1_matches[(p1_matches['tourney_date'] == date) & (p1_matches['match_num'] >= row['match_num'])].index
    )
    p1_matches.reset_index(inplace=True)
    p1_match = p1_matches.tail(1)

    if p1_match.shape[0] > 0:
        if np.isnan(p1_match.iloc[0]['w_1stWon']):
            p1_stat = 0.7
        else:
            if p1 == p1_match.iloc[0]['winner_id']:
                p1_stat = (p1_match.iloc[0]['w_1stWon'] + p1_match.iloc[0]['w_2ndWon']) / p1_match.iloc[0]['w_svpt']
            else:
                p1_stat = (p1_match.iloc[0]['l_1stWon'] + p1_match.iloc[0]['l_2ndWon']) / p1_match.iloc[0]['l_svpt']
    else:
        p1_stat = 0.7

    p2_matches = df.loc[
        ((df['winner_id'] == p2) | (df['loser_id'] == p2)) &
        (df['tourney_date'] <= date)
        ]
    p2_matches = p2_matches.drop(
        p2_matches[(p2_matches['tourney_date'] == date) & (p2_matches['match_num'] >= row['match_num'])].index
    )
    p2_matches.reset_index(inplace=True)
    p2_match = p2_matches.tail(1)
    if p2_match.shape[0] > 0:
        if np.isnan(p2_match.iloc[0]['w_1stWon']):
            p2_stat = 0.7
        else:
            if p2 == p2_match.iloc[0]['winner_id']:
                p2_stat = (p2_match.iloc[0]['w_1stWon'] + p2_match.iloc[0]['w_2ndWon']) / p2_match.iloc[0]['w_svpt']
            else:
                p2_stat = (p2_match.iloc[0]['l_1stWon'] + p2_match.iloc[0]['l_2ndWon']) / p2_match.iloc[0]['l_svpt']
    else:
        p2_stat = 0.7

    return p1_stat, p2_stat


def wl_record_last_x_matches(data, x):
    print('wl_record_last_x_matches')
    print(datetime.datetime.now())

    v1s, v2s, v3s, v4s = [], [], [], []
    for _, row in data.iterrows():
        v1, v2, v3, v4 = players_results(data, row, x_matches=x)
        v1s.append(v1)
        v2s.append(v2)
        v3s.append(v3)
        v4s.append(v4)

    df_result = pd.DataFrame({'P1WX': v1s,
                              'P1LX': v2s,
                              'P2WX': v3s,
                              'P2LX': v4s
                              })

    df_result.to_csv('my_files/wl_last_15_matches.csv', index=False, float_format='%g')
    return df_result


def wl_record_this_tournament(data):
    print('wl_record_this_tournament')
    print(datetime.datetime.now())

    v1s, v2s, v3s, v4s = [], [], [], []
    for _, row in data.iterrows():
        v1, v2, v3, v4 = players_results(data, row, this_tournament=True)
        v1s.append(v1)
        v2s.append(v2)
        v3s.append(v3)
        v4s.append(v4)

    df_result = pd.DataFrame({'P1WT': v1s,
                              'P1LT': v2s,
                              'P2WT': v3s,
                              'P2LT': v4s
                              })

    df_result.to_csv('my_files/wl_this_tournament.csv', index=False, float_format='%g')
    return df_result


def serve_index(data):
    print('serve_index')
    print(datetime.datetime.now())

    v1s, v2s = [], []
    for _, row in data.iterrows():
        v1, v2 = last_match_stats(data, row)
        v1s.append(v1)
        v2s.append(v2)

    df_result = pd.DataFrame({'P1serve_index': v1s,
                              'P2serve_index': v2s
                              })

    df_result.to_csv('my_files/serve_index.csv', index=False, float_format='%g')
    return df_result


if __name__ == '__main__':
    df = pd.read_csv('my_files/raw.csv', low_memory=False)

    wlx = wl_record_last_x_matches(df, 15)
    wlt = wl_record_this_tournament(df)
    si = serve_index(df)

    # df.reset_index(inplace=True, drop=True)
    df_wlx = pd.concat([df, wlx], axis=1)
    df_wlt = pd.concat([df, wlt], axis=1)
    df_si = pd.concat([df, si], axis=1)
    df_wlx.to_csv('my_files/raw_with_wlx.csv', index=False, float_format='%g')
    df_wlt.to_csv('my_files/raw_with_wlt.csv', index=False, float_format='%g')
    df_si.to_csv('my_files/raw_with_serve_index.csv', index=False, float_format='%g')


    # wl_record_this_tournament(df)
    # wl_record_this_surface(df)
