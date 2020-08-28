#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:28:45 2020

@author: mati
"""

import os
name = os.path.basename(__file__).split(".py")[0]
import pandas as pd
import sys
sys.path.append('/home/mati/Storage/Tesis/AnalisisGo-Tesis')
#sys.path.append('/home/mmazzanti/AnalisisGo-Tesis')
import src as thM
from importlib import reload
from collections import defaultdict
import pickle

reload(thM)

df = pd.read_csv('./KGS_filtered.csv')
#df = df[:50000]  # por si solo nos quedamos con una base reducida

print(df.shape)
df = df[(~df.white.str.contains('bot',case=False, na=False))&(~df.black.str.contains('bot',case=False, na=False))]
df=df[df.white!=df.black]

#Nos quedamos con tamaño 19
df = df[df.width==19]

# Si queremos armar baches por meses
df['date'] = df['started'].apply(lambda row: row[0:7])
df = df[df.date.str.contains('2007') | df.date.str.contains('2008')]
print(df.date.head())
fecha = 0
dates = []
count = 0
for i in df.index:
    if df.loc[i].date == fecha:
        dates.append(count)
    else:
        print(count)
        count += 1
        dates.append(count)
    fecha = df.loc[i].date
df['date'] = dates

# si queremos armar baches por años
#df['date'] = df['started'].apply(lambda row: row[0:4])
#df = df[df.date.str.contains('2007')|df.date.str.contains('2008')|df.date.str.contains('2009')|df.date.str.contains('2010')]
df['date'] = df.date.apply(lambda x: int(x))
# agrego cero a los handicaps nulos
df.handicap = df.handicap.apply(lambda x: x if x>=2 else 0)

# me quedo solo con komis normales
df = df[(df.komi==0.5)|(df.komi==5.5)|(df.komi==6.5)|(df.komi==7.5)]
df = df[(df.whiteRank.str.contains('d'))&(df.blackRank.str.contains('d'))]
df = df[['id', 'black', 'white',  'black_win', 'handicap', 'komi',
        'width', 'date', 'whiteRank', 'blackRank', 'started']]
df = df.sort_values(by=['date', 'id'])
df = df.reset_index()
print(df.shape)

df.to_csv("./KGS_filtered_julia_meses.csv", index=False)
#df.to_csv("./KGS_filtered_julia.csv", index=False)
