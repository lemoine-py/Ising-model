
"""
This program is a demonstration of the Ising model simulation 
for a range of increasing temperature values. 
"""

from Range_temp import Ising_Range_temp
from Initialize import title,endroll

### Parameters :

N = 100 # Lattice size
matrix_type = "r" # initial matrix type : "r" for random, "u" for all-up, "d" for all-down
J, B = 1,0.2 # Coupling interaction, magnetic field
edge = "c" # edge conditions : "c" for edge-closed-square, "t" for edge-connected-torus

### Calling the main function :
title()
Ising_Range_temp(N, matrix_type, J, B, edge)
endroll()