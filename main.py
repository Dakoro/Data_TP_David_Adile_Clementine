import matplotlib.pyplot as plt
import scipy.stats as stat
import numpy as mp
from matplotlib.ticker import PercentFormatter
import pandas as pd
from colorama import Fore, Back, Style
%matplotlib inline

def plot_pareto_by(df, x, y, hlines=[80]):

    df['Cumulative Percentage'] = df[y].cumsum()/df[y].sum()*100
    
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(df[x], df[y], color='C0')
    ax2 = ax.twinx()
    ax2.plot(df[x], df['Cumulative Percentage'], color='C1', ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter())
    ax.tick_params(axis='y', colors='C0')
    ax2.tick_params(axis='y', colors='C1')

    for tick in ax.get_xticklabels():
        tick.set_rotation(90)

    plt.title(f'Pareto Chart for {y} by {x}')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax2.set_ylabel('Cumulative Percentage')

    for hline_at in hlines:
        ax2.axhline(y=hline_at, color='red', linestyle='-.')
    plt.show()


# Récupération de la liste de CSV si fournie
# Ou utilisation de glob

fns = !ls fao_2013/*.csv
# Lecture puis affichage des info taille des CSV
df_animal = pd.read_csv(fns[0])
df_pop = pd.read_csv(fns[1])
df_alim = pd.read_csv(fns[2])
df_veg = pd.read_csv(fns[3])
