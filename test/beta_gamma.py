import os
name = os.path.basename(__file__).split(".py")[0]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('./matrix_ev.csv')


betas = list(df['betas'].to_numpy())

gammas = list(df.columns)
gammas = gammas[1:]
for i in range(len(gammas)):
    gammas[i] = gammas[i].strip('Gamma=')
    gammas[i] = float(gammas[i])

df = df.drop(['betas'],axis=1)

plt.pcolor(betas,gammas,Matrix, cmap='RdBu', vmin=z_min, vmax=z_max, rasterized=True)
