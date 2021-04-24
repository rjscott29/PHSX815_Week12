import numpy as np
import matplotlib.pyplot as plt

# define number of games and number of experiments
Ng = 100
Ne = 10000
# define llambda for poisson distribution
llambda = 2

# returns n values from poisson distribution
def nGames(n, llambda):
    values = []
    for x in range(0,n):
        values.append(np.random.poisson(llambda))
    return values

# returns Ne number of averaged games from Ng number of games
def nExp(Ne, Ng, llambda):
    ExpValues = []
    for x in range(0,Ne):
        ExpValues.append(np.mean(nGames(Ng, llambda)))
    return ExpValues

plt.figure()

plt.hist(nExp(Ne, Ng, llambda))

plt.show()