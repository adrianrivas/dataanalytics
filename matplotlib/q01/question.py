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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas
df = pandas.read_csv('data.csv', sep=',', encoding='latin-1')
data = df.groupby('Region').sum()[['Poblacion 0-14', 'Poblacion 15-64', 'Poblacion 65+']]
data[['Poblacion 0-14', 'Poblacion 15-64', 'Poblacion 65+']]
figura, eje = plt.subplots(1, 6, sharex='col', sharey='row', figsize=(13, 6), dpi=72);
plt.subplots_adjust(wspace = 0.1, hspace=0.1)
plt.setp(eje[0], ylabel='Poblacion')
for i in range(len(data)):
    eje[i].scatter(list(data.iloc[i].index), data.iloc[i][['Poblacion 0-14', 'Poblacion 15-64', 'Poblacion 65+']], marker='o', facecolors='none', linewidth = 3, edgecolors = ['tab:orange', 'tab:blue', 'tab:green'], s=200);
    eje[i].set_xlim(-0.30,2.30)
for n, ax in enumerate(eje):
  ax.set_xticks(range(3));
  ax.set_xticklabels(data.columns, rotation=90);
  ax.set_title(data.index[n]);
plt.tight_layout() 
plt.savefig('generada.png')