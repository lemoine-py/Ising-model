
""" 
This program is a demonstration of the Ising model simulation 
for a fixed temperature value. 
"""

from Metropolis import matrix_generator
from Fixed_temp import Ising_Fix_temp

### Parameters :

N = 100 # Lattice size
matrix_type = "r" # initial matrix type : "r" for random, "u" for all-up, "d" for all-down
S_0 = matrix_generator(N, matrix_type)
J, B, T = 1,0.2,0.5 # Coupling interaction, magnetic field, temperature
edge = "t" # edge conditions : "c" for edge-closed-square, "t" for edge-connected-torus

### Calling the main function :
    
Ising_Fix_temp(N,S_0,J,B,T,edge)
