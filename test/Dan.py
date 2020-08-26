import os
name = os.path.basename(__file__).split(".py")[0]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


path = '/home/mati/Storage/Tesis/AnalisisGo-Tesis/Julia/test/KGS_filtered_julia.csv'
df = pd.read_csv(path)
#df = pd.read_csv('./KGS_filtered_julia_reducido.csv')
#%%
df.whiteRank = df.whiteRank.replace({'d': ''}, regex=True)
df.blackRank = df.blackRank.replace({'d': ''}, regex=True)
df.whiteRank = df.whiteRank.apply(lambda x: int(x))
df.blackRank = df.blackRank.apply(lambda x: int(x))
#%%
Blanco = df[["white", "started", 'whiteRank']]
Negro = df[["black", "started", 'blackRank']]

df2 = pd.DataFrame(np.concatenate((Blanco.values, Negro.values), axis=0))
df2.columns = ['Jugador', 'Tiempo', 'Rango']
df2 = df2.sort_values(by=["Jugador", "Tiempo"])

# Cantidad de partidas por jugador
Cuentas = df2["Jugador"].value_counts()
JugadorMax = Cuentas.index[0]
JugadorMaxdf = df2[df2["Jugador"] == JugadorMax]
JugadorMaxdf = JugadorMaxdf.sort_values(by=["Tiempo"]).reset_index(drop=True)
JugadorMaxdf = JugadorMaxdf.reset_index()

#%%
numeroJugadores = 3
plt.figure(0)
#xlimSigma = max(JugadorMaxdf.index)
xlimSigma = 1000
plt.axis([-10, xlimSigma, 0, 10])

count = 0
for i in range(numeroJugadores):  # me cambia el eje x, siempre se redefine.
    Jugador1 = Cuentas.index[count+1]
    Jugador1df = df2[df2["Jugador"] == Jugador1]
    Jugador1df = Jugador1df.sort_values(by=["Tiempo"]).reset_index(drop=True)
    Jugador1df = Jugador1df.reset_index()
    index = Jugador1df.index.values
    Rango = Jugador1df.Rango.values
    count += 1
    plt.plot(index, Rango, label=f'Jugador {i}')

plt.xlabel('Numero de Partidas')
plt.ylabel('Rango')
plt.xlim(0, 90)
plt.legend()
plt.show()
