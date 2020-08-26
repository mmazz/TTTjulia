# -*- coding: utf-8 -*-
import pandas as pd
import json

csv_name = './parser.csv'

print("Dataframe metida")
df = pd.read_csv(csv_name)
print(df.shape)
df = df[['id', 'black', 'white', 'order', 'outcome', 'handicap', 'komi',
        'width', 'started', 'whiteRank', 'blackRank']]

print("Total: ", df.shape)
df = df[(df["width"] >= 9) & (df["width"] <= 19)]
print("Tamaño estandar: ", df.shape)
df = df[(df.order == 1) | (df.order == 0)]
print("Resultado estandar: ", df.shape)

df['black_win'] = df.order

def outcomeOutput(x):
    if 'Resign' in x:
        x = 'Resign'
    elif 'Time' in x:
        x = 'Time'
    else:
        x=x


#df.outcome = df.outcome.apply(lambda x: outcomeOutput(x))
df = df[['id', 'black', 'white', 'outcome', 'black_win', 'handicap', 'komi',
        'width', 'started', 'whiteRank', 'blackRank']]
# Ordeno
df = df.sort_values(by=['started', 'id'])

df = df.reset_index()
print(df.shape)
df.to_csv("./KGS_filtered.csv", index=False)
