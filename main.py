import matplotlib.pyplot
import scipy.stats as stat
import numpy as mp
import glob, sys
import pandas as pd
from colorama import Fore, Back, Style
# %matplotlib inline





# Récupération de la liste de CSV si fournie
# Ou utilisation de glob

fns = sys.argv[1:]
if not fns:
    fns = glob.glob('fao_2013/*.csv')

# Lecture puis affichage des info taille des CSV
for fn in fns:
    fns = fn[22:-4]
    df = pd.read_csv(fn)
    print(f"- {fn:50s} ({df.shape[0]:6d}, {df.shape[1]:2d}) - {Fore.BLACK}{Back.GREEN}{fns}{Style.RESET_ALL}")

