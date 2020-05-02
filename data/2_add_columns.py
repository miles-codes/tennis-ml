import pandas as pd
import datetime

from data.utils import h2h, players_results


# 15 min runtime
def h2h_(data):
    v1s, v2s = [], []
    for _, row in data.iterrows():
        v1, v2 = h2h(data, row)
        v1s.append(v1)
        v2s.append(v2)
    df_result = pd.DataFrame({'H2HW': v1s,
                              'H2HL': v2s,
                              })

    df_result.to_csv('csv_files/h2h.csv', index=False, float_format='%g')


# 30 min runtime
def wl_record(data):
    start = datetime.datetime.now()

    v1s, v2s, v3s, v4s = [], [], [], []
    for _, row in data.iterrows():
        v1, v2, v3, v4 = players_results(data, row)
        v1s.append(v1)
        v2s.append(v2)
        v3s.append(v3)
        v4s.append(v4)

    print(datetime.datetime.now() - start)

    df_result = pd.DataFrame({'P1W': v1s,
                              'P1L': v2s,
                              'P2W': v3s,
                              'P2L': v4s
                              })

    df_result.to_csv('csv_files/wl.csv', index=False, float_format='%g')


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

    df_result.to_csv('csv_files/wl_last_x_matches.csv', index=False, float_format='%g')


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

    df_result.to_csv('csv_files/wl_this_tournament.csv', index=False, float_format='%g')


def wl_record_this_surface(data):
    print('wl_record_this_surface')
    print(datetime.datetime.now())

    v1s, v2s, v3s, v4s = [], [], [], []
    for _, row in data.iterrows():
        v1, v2, v3, v4 = players_results(data, row, this_surface=True)
        v1s.append(v1)
        v2s.append(v2)
        v3s.append(v3)
        v4s.append(v4)

    df_result = pd.DataFrame({'P1WS': v1s,
                              'P1LS': v2s,
                              'P2WS': v3s,
                              'P2LS': v4s
                              })

    df_result.to_csv('csv_files/wl_this_surface.csv', index=False, float_format='%g')


if __name__ == '__main__':
    df = pd.read_csv('csv_files/full_data.csv', low_memory=False)
    wl_record_last_x_matches(df, 10)
    wl_record_this_tournament(df)
    wl_record_this_surface(df)
