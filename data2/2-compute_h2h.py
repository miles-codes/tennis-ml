import datetime

import pandas as pd
import numpy as np

# START_DATE = 19901231


def init_h2h():
    raw = pd.read_csv('my_files/raw.csv')
    winners = raw.winner_name.unique()
    losers = raw.loser_name.unique()
    players = np.concatenate((winners, losers))
    players = np.unique(players)
    matrix = np.zeros((players.size, players.size), dtype=np.uint8)

    h2h_df = pd.DataFrame(matrix, index=players, columns=players)
    h2h_df.to_csv('my_files/h2h.csv')


if __name__ == '__main__':
    start = datetime.datetime.now()
    # init_h2h()

    df = pd.read_csv('my_files/raw.csv')
    df_h2h = pd.read_csv('my_files/h2h.csv', index_col=0)
    v1s, v2s = [], []
    for _, row in df.iterrows():
        v1 = df_h2h.loc[row['winner_name'], row['loser_name']]
        v2 = df_h2h.loc[row['loser_name'], row['winner_name']]
        v1s.append(v1)
        v2s.append(v2)
        df_h2h.loc[row['winner_name'], row['loser_name']] += 1
    df_result = pd.DataFrame({'w_h2h': v1s,
                              'l_h2h': v2s,
                              })
    # df.reset_index(inplace=True, drop=True)
    aaa = pd.concat([df, df_result], axis=1)
    aaa.to_csv('my_files/raw_h2h.csv', index=False, float_format='%g')
    #
    print(datetime.datetime.now() - start)
