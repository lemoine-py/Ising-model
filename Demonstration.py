""" This program is a demonstration of the different sorts of simulations and plots that
the present Ising model in 2D is capable to produce.
The program just needs to be run, without any interaction with the user (no inputs).
All the parameters are already set to default values.
"""

from Metropolis import rnd_matrix

### Parameters :

N = 100
S_0 = rnd_matrix(N)
J = 1
B = 1
T = 1

# dictionnary of parameters then use **kwargs in the functions ?

#...

from Ising_main import Ising_model

Ising_model()