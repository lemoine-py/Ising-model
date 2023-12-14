
"""
LPHYS1201 : Informatique et méthodes numériques
Date : Authors: Solal Lemoine, Etienne Roger
Project name : Ising Model
Description : Simulation of the ferromagnetic properties of materials 
in a 2D lattice, with the Metropolis algorithm and graphical representation.
"""

from Initialize import Initialize_Ising
from Fixed_temp import Ising_Fixed_temp
from Range_temp import Ising_Range_temp
from Metropolis import endroll

import time
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
    def __exit__(self, type, value, traceback):
        print("Total run time:", time.perf_counter() - self.start)


def Ising_model():
    """ Main function that runs the whole Ising model simulation process"""
    
    
    N, matrix_type, S_0, J, B, model, edge, boundary = Initialize_Ising()
    
    with Timer():
        if model == "f":
            from Fixed_temp import Ising_Fixed_temp
            Ising_Fixed_temp()
        elif model == "r":
            from Range_temp import Ising_Range_temp
            Ising_Range_temp()
        
    endroll()
 

Ising_model()



