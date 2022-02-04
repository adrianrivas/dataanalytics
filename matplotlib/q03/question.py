##
##  Graficacion usando Matplotlib
##  ===========================================================================
##
##  Construya una gráfica similar a la presentada en el archivo `original.png`
##  usando el archivo `data.csv`. La gráfica generada debe salvarse en el 
##  archivo `generada.png`. 
##
##  Salve la figura al disco con:
##
##     plt.savefig('generada.png')
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv', sep=',')
data = df.groupby('Region').sum()[['Poblacion 0-14', 'Poblacion 15-64', 'Poblacion 65+']]
fig, axs = plt.subplots(3, 1, sharex='col', sharey='row', figsize=(8,10), dpi=72);
plt.subplots_adjust(wspace = 0.1, hspace=0)
axs[0].bar(range(6), data.iloc[:,0], color='tab:orange')
axs[1].bar(range(6), data.iloc[:,1], color='tab:blue')
axs[2].bar(range(6), data.iloc[:,2], color='tab:green')
for n, ax in enumerate(axs):
  ax.set_xticks(range(6));
  ax.set_xticklabels(data.index, rotation=90);
  ax.set_ylabel(data.columns[n])
  ax.spines['top'].set_visible(False)
  ax.spines['left'].set_visible(False)
  ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('generada.png')