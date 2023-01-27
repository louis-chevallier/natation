import pandas as pd
import pulp as plp
import numpy as np
from utillc import *

# les nageurs

# donne des perf au hasard
s = lambda : int(np.random.normal(0) * 10 + 100)
K=4 # 4 nages
nageur = lambda _ : [ s() for _ in range(K)]
N,T=12, 5 # 12 nageurs, en choisir 5
nageurs = np.asarray(list(map(nageur, range(N))))

df = pd.DataFrame(nageurs, columns = ['brasse', 'crawl', 'papillon', 'dos'])
EKOX(df)

# on veut minimiser l'objectif
problem = plp.LpProblem('Natation', plp.LpMinimize)

# N variables binaires qui sélectionnent les nageurs
sel = plp.LpVariable.dicts("Choice", range(N), cat="Binary")

# on ne veut selectyionner que  T  
problem += plp.lpSum([ sel[n] for n in range(N) ]) == T

# et l'objectif est la somme des temps des sélectionnés
problem += plp.lpSum([ nageurs[n,k] * sel[n] for n in range(N) for k in range(K) ])
    
problem.solve()
EKOX(plp.LpStatus[problem.status])
EKOX(sel)
for v in problem.variables():  EKON(v.name, v.varValue)

