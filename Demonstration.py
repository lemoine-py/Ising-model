""" This program is a demonstration of the different sorts of simulations and plots that
the present Ising model in 2D is capable to produce.
The program just needs to be run, without any interaction with the user (no inputs).
All the parameters are already set to default values.
"""

from Metropolis import matrix_generator
from Fixed_temp import Ising_Fixed_temp
from Range_temp import Ising_Range_temp


### Parameters :

N = 100
matrix_type = "r"
S_0 = matrix_generator(N,matrix_type)

J = 1
B = 1
T = 1

edge = "c"

Ising_Fixed_temp(N,S_0,J,B,T,edge)

Ising_Range_temp(N,matrix_type,S_0,J,B,T,edge)