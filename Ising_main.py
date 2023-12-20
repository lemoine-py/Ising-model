
"""
LPHYS1201 : Informatique et méthodes numériques
Authors: Solal Lemoine, Etienne Roge
Date : december 2023
Project name : Ising Model
Description : Simulation of the ferromagnetic properties of materials 
in a 2D lattice, with the Metropolis algorithm and graphical representation.
"""

from Initialize import Initialize_Ising
from Fixed_temp import Ising_Fix_temp
from Range_temp import Ising_Range_temp

def Ising_model():
    """ Main function that runs the whole Ising model simulation process.
    
        Firstly, Initialize_Ising() is called : the user has to enter 
        the simulation's parameters. 
        Then it is redirected to either :
        Ising_Fix_temp(...) or Ising_Range_temp(...) according to the 'model'
        that was chosen.
    """

    N, matrix_type, S_0, J, B, model, T, edge = Initialize_Ising()

    if model == "f":
        Ising_Fix_temp(N,S_0,J,B,T,edge)
    elif model == "r":
        Ising_Range_temp(N,matrix_type,S_0,J,B,T,edge)

    print("\n =============== END of the Ising model simulation =============== \n")

Ising_model()