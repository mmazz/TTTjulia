#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:00:17 2020

@author: mati
"""
import os
name = os.path.basename(__file__).split(".py")[0]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


df= pd.read_csv('./Trueskill_datos_con_handicap.csv')
df_h = pd.read_csv('./Trueskill_datos_vs_trueskill.csv')
df_TTT = pd.read_csv('./TTT_datos_sin_handicap.csv')
df_TTT_h= pd.read_csv('./TTT_datos_vs_trueskill.csv')



#%%
evidencia = df[['evidence']].values
evidencia_h = df_h[['evidence']].values
evidencia_TTT = df_TTT[['evidence']].values
evidencia_TTT_h = df_TTT_h[['evidence']].values

evidencia = sum([-math.log(x) for x in evidencia])/len(evidencia)
evidencia_h = sum([-math.log(x) for x in evidencia_h])/len(evidencia_h)
evidencia_TTT = sum([-math.log(x) for x in evidencia_TTT])/len(evidencia_TTT)
evidencia_TTT_h = sum([-math.log(x) for x in evidencia_TTT_h])/len(evidencia_TTT_h)

print(evidencia, evidencia_h,evidencia_TTT,evidencia_TTT_h)
