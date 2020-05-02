import pandas as pd


def rank_ratio(row):
    if row['B365W'] <= row['B365L']:
        return row['LRank'] / row['WRank']
    else:
        return row['WRank'] / row['LRank']


def odds_ratio(row, c1, c2):
    return max(row[c1], row[c2]) / min(row[c1], row[c2])


def h2h_ratio(row):
    if row['B365W'] <= row['B365L']:
        return row['H2HW'] - row['H2HL']
    else:
        return row['H2HL'] - row['H2HW']


def win_loss_ratio(row, c1, c2, c3, c4):
    if row[c1] != 0 and row[c2] != 0:
        wlw = row[c1] / row[c2]
    else:
        wlw = row[c1] - row[c2]

    if row[c3] != 0 and row[c4] != 0:
        wll = row[c3] / row[c4]
    else:
        wll = row[c3] - row[c4]

    if row['B365W'] <= row['B365L']:
        if wlw != 0 and wll != 0:
            return wlw / wll
        else:
            return wlw - wll
    else:
        if wlw != 0 and wll != 0:
            return wll / wlw
        else:
            return wll - wlw


df = pd.read_csv('csv_files/selected_features.csv')

df['RankRatio'] = df.apply(lambda row: rank_ratio(row), axis=1)
df['B365Ratio'] = df.apply(lambda row: odds_ratio(row, 'B365W', 'B365L'), axis=1)
df['H2HRatio'] = df.apply(lambda row: h2h_ratio(row), axis=1)
df['WLRatio'] = df.apply(lambda row: win_loss_ratio(row, 'P1W', 'P1L', 'P2W', 'P2L'), axis=1)
df['WLXRatio'] = df.apply(lambda row: win_loss_ratio(row, 'P1WX', 'P1LX', 'P2WX', 'P2LX'), axis=1)
df['WLTRatio'] = df.apply(lambda row: win_loss_ratio(row, 'P1WT', 'P1LT', 'P2WT', 'P2LT'), axis=1)
df['WLSRatio'] = df.apply(lambda row: win_loss_ratio(row, 'P1WS', 'P1LS', 'P2WS', 'P2LS'), axis=1)
df['output'] = df['B365W'] <= df['B365L']

df.drop([
    'WRank', 'LRank',
    'B365W', 'B365L',
    'H2HW', 'H2HL',
    'P1W', 'P1L', 'P2W', 'P2L',
    'P1WX', 'P1LX', 'P2WX', 'P2LX',
    'P1WT', 'P1LT', 'P2WT', 'P2LT',
    'P1WS', 'P1LS', 'P2WS', 'P2LS'
], axis=1, inplace=True)

print((df.output == 1).sum())
print((df.output == 0).sum())
print(df.shape)

df.to_csv('csv_files/ready.csv', index=False, float_format='%g')
