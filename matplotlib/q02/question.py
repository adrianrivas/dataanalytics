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
fig, axs = plt.subplots(1, 6, sharex='col', sharey='row', figsize=(13,6), dpi=72);
plt.subplots_adjust(wspace = 0.1, hspace=0.1)
plt.setp(axs[0], ylabel='Poblacion')
for index, region in enumerate(data.index):
    axs[index].bar(range(3), data.iloc[index,:], color=['tab:orange', 'tab:blue', 'tab:green'])
for n, ax in enumerate(axs):
  ax.set_xticks(range(3));
  ax.set_xticklabels(data.columns, rotation=90);
  ax.set_title(data.index[n]);
plt.tight_layout()
plt.savefig('generada.png');