import os
name = os.path.basename(__file__).split(".py")[0]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('./data_set.csv')

skills = [df[df.handicap==i].iloc[-1].h_mean for i in range(2,10)]
sigmas = [df[df.handicap==i].iloc[-1].h_std for i in range(2,10)]
NumeroPartidas = []
for i in range(2,10):
    NumeroPartidas.append(df[df.handicap==i].handicap.value_counts().iloc[0])
handicaps = list(range(2,10))
skills_sigmas = np.zeros(len(skills))
skills_sigmas2 = np.zeros(len(skills))
skills_sigmas3 = np.zeros(len(skills))
skills_sigmas4 = np.zeros(len(skills))

for i in range(len(skills)):
    skills_sigmas[i] = skills[i]+2*sigmas[i]
    skills_sigmas2[i] = skills[i]-2*sigmas[i]
    skills_sigmas3[i] = skills[i]+sigmas[i]
    skills_sigmas4[i] = skills[i]-sigmas[i]

plt.figure(0)

plt.plot([handicaps, handicaps], [skills_sigmas, skills_sigmas2], linewidth=0.5, color='grey')
plt.plot([handicaps, handicaps], [skills_sigmas3, skills_sigmas4], linewidth=1, color='black')
plt.scatter(handicaps, skills, label=f'H9- #Partidas={NumeroPartidas}')
plt.legend()
plt.show()
