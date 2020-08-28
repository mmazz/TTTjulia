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


path = '/home/mati/Storage/Tesis/AnalisisGo-Tesis/Julia/test/TTT_datos_reducido.csv'
df = pd.read_csv(path)
#%%
Blanco = df[["white","w_mean","w_std" ]]
Negro = df[["black","b_mean","b_std"]]

df2 = pd.DataFrame( np.concatenate( (Blanco.values, Negro.values), axis=0 ) )
df2.columns = ['Jugador', 'Mu', 'Sigma']
df2.Mu = pd.to_numeric(df2.Mu)
df2.Sigma = pd.to_numeric(df2.Sigma)
df2 = df2.sort_values(by=["Jugador"])
# %%

Cuentas = df2["Jugador"].value_counts()
JugadorMax = Cuentas.index[0]
JugadorMaxdf = df2[df2["Jugador"] == JugadorMax]
#JugadorMaxdf = JugadorMaxdf.sort_values(by=["timestart"]).reset_index(drop=True)
JugadorMaxdf = JugadorMaxdf.reset_index()

#%%
paso_jugadores = 10  # antes era 100
numeroJugadores = 10
plt.figure(0)
#xlimSigma = max(JugadorMaxdf.index)
xlimSigma = 1000
plt.axis([-10, xlimSigma, 0, 10])

count = 0
for i in range(numeroJugadores): # me cambia el eje x, siempre se redefine.
    Jugador1 = Cuentas.index[count]
    Jugador1df = df2[df2["Jugador"] == Jugador1]
    #Jugador1df = Jugador1df.sort_values(by=["timestart"]).reset_index(drop=True)
    Jugador1df = Jugador1df.reset_index()
    index = Jugador1df.index.values
    Sigma = Jugador1df.Sigma.values
    count += paso_jugadores
    plt.plot(index,Sigma, label=f'Jugador {i}')

plt.xlabel('Numero de Partidas')
plt.ylabel('Sigma')
plt.xlim(0,90)
plt.legend()
plt.show()

#%%

plt.figure(1)
xlimSigma = 1000
plt.axis([-10, xlimSigma, 10, 50])

count = 0
for i in range(numeroJugadores): # me cambia el eje x, siempre se redefine.
    Jugador1 = Cuentas.index[count]
    Jugador1df = df2[df2["Jugador"] == Jugador1]
    #Jugador1df = Jugador1df.sort_values(by=["timestart"]).reset_index(drop=True)
    Jugador1df = Jugador1df.reset_index()
    index = Jugador1df.index.values
    Mu = Jugador1df.Mu.values
    count += paso_jugadores
    plt.plot(index,Mu, label=f'Jugador {i}')

    #fig1, ax1 = plt.subplots()
    #Jugador1df.plot(kind='scatter',x='index',y='Mu', color='Blue',ax=ax1)
plt.xlabel('Numero de Partidas')
plt.ylabel('Mu')
plt.xlim(-5,500)
plt.legend()
plt.show()

# %%
