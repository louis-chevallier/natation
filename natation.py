import pandas as pd
import pulp as plp
import numpy as np
from utillc import *

# les nageurs
s = lambda : int(np.random.normal(0) * 10 + 100)
K=4
nageur = lambda _ : [ s() for _ in range(K)]
N,T=12, 5
nageurs = np.asarray(list(map(nageur, range(N))))

df = pd.DataFrame(nageurs, columns = ['brasse', 'crawl', 'papillon', 'dos'])
EKOX(df)

problem = plp.LpProblem('Natation', plp.LpMinimize)
sel = plp.LpVariable.dicts("Choice", range(N), cat="Binary")
problem += plp.lpSum([ sel[n] for n in range(N) ]) == T
problem += plp.lpSum([ nageurs[n,k] * sel[n] for n in range(N) for k in range(K) ])
    
problem.solve()
EKOX(plp.LpStatus[problem.status])
EKOX(sel)
for v in problem.variables():  EKON(v.name, v.varValue)

