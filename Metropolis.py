"""
This program contains the basic functions for the Metropolis algorithm.
(And a few other utilities)
"""

import numpy as np
import time

### Initial configuration :
def rnd_matrix(N):
    """ Generates and returns a NxN matrix with randomly up or down spins.
        Argument : N (int)
    """
    spins = (1,-1)
    matrix = np.random.choice(spins,size=(N,N))
    return matrix

def up_matrix(N):
    """ Generates and returns a NxN matrix with only up spins."""
    matrix = np.ones((N,N))
    return matrix
# Just multiply up_matrix by -1 if a "down_matrix" is needed.

def matrix_generator(N,matrix_type):
    if matrix_type == "r":
        S_0 = rnd_matrix(N)
    elif matrix_type == "u":
        S_0 = up_matrix(N)
    elif matrix_type == "d":
        S_0 = - up_matrix(N)
    return S_0

### Spin modification :   
def ij_generate(N):
    """Randomly generates two numbers, used later to access a random spin"""
    i,j = tuple(np.random.randint(N,size=2))
    return i,j

def flip_spin(i,j,S_0):
    """ Returns  """
    S_1 = np.copy(S_0)
    S_1[i][j] *= -1
    return S_1


### Energy calculator :
def local_energy_J(i,j,S_0,J,edge):
    """ Returns the local energy due to coupling J. """
    loc_energy_J = 0
    if i != 0:
        loc_energy_J -= J*S_0[i-1][j]*S_0[i][j]
    if j != 0:
        loc_energy_J -= J*S_0[i][j-1]*S_0[i][j]
    if i != len(S_0)-1:
        loc_energy_J -= J*S_0[i+1][j]*S_0[i][j]
    if j != len(S_0)-1:
        loc_energy_J -= J*S_0[i][j+1]*S_0[i][j]
        
    if edge == "t":
        if i == 0:
            loc_energy_J -= J*S_0[len(S_0)-1][j]*S_0[i][j]
        if i == len(S_0)-1:
            loc_energy_J -= J*S_0[0][j]*S_0[i][j]
        if j == 0:
            loc_energy_J -= J*S_0[i][len(S_0)-1]*S_0[i][j]
        if j == len(S_0)-1:
            loc_energy_J -= J*S_0[i][0]*S_0[i][j]     
    return loc_energy_J

def local_energy_B(i,j,S_0,B):
    """ Returns the local energy due to magnetic field B. """
    loc_energy_B = 0
    loc_energy_B -= B*S_0[i][j]
    return loc_energy_B

def local_energy(i,j,S_0,J,B,edge):
    """ Returns the sum of the two local energies.
        Arguments : i (int), j (int), S_0 (matrix), B (float), J (float), edge (str)
    """
    return local_energy_J(i,j,S_0,J,edge) + local_energy_B(i,j,S_0,B)

def total_energy(S_0,J,B,edge):
    """Returns the total energy of the entire lattice."""
    energy = 0
    i = 0
    while i < len(S_0):
        j = 0
        while j < len(S_0):
            energy += (local_energy_J(i,j,S_0,J,edge)/2) + local_energy_B(i,j,S_0,B) 
            j += 1
        i += 1
    return energy

def delta_E(loc_E_0,loc_E_1):
    """Returns the energy difference after a spin flip."""
    dE = loc_E_1 - loc_E_0
    return dE


### Accepting or rejecting the spin modification:   
def accept_flip(S_0,S_1,dE,T):
    """Accepts or rejects the random spin flip, based on delta_E and T.
    Arguments: S_0 (matrix), delta_E (float), T (float)
    Return: S_0 (modified matrix), flip (boolean)""" 
    if dE < 0:
        S_0 = S_1
        flip = True
    else:
        if np.random.uniform(0,1) < np.exp(-dE/T):
            S_0 = S_1
            flip = True
        else:
            flip = False
    return S_0, flip

### Metropolis algorithm (for one temperature lefvel) :

def Metropolis(N, matrix_type, S_0, J, B, model, T, edge, boundary):
    k = 0
    k_max = 15*(N**2) 
    while k <= k_max: 
        i, j = ij_generate(N) # Random index
        S_1 = flip_spin(i, j, S_0) # New matrix with one flipped spin
        loc_E0 = local_energy(i, j, S_0, J, B, edge) # S_0's local energy
        loc_E1 = local_energy(i, j, S_1, J, B, edge) # S_1's local energy
        dE = delta_E(loc_E0, loc_E1) # Energy difference
        S_0, flip = accept_flip(S_0, S_1, dE, T) # Validating or rejecting the flip
        k+=1


###### Other utilities :
    
### Magnetization calculator
def magnetic(S_0):
    """Magnetization (sum of all spin values) of the given lattice"""
    magnet = sum(sum(S_0))
    return magnet


### Timer decorator  :
def timer(function):
    def timed_function(*args, **kwargs):
        t_start = time.perf_counter()
        out = function(*args, **kwargs)
        print(f" --- Total time : {time.perf_counter() - t_start:.2f} seconds")
        return out
    return timed_function

### Program's end message :
def endroll():
    print("\n =============== END =============== \n")


if __name__ == "__main__":
    from Initialize import Initialize_Ising
    N,matrix_type, S_0,J,B,model,T,edge,boundary = Initialize_Ising()
    Metropolis(N, matrix_type, S_0, J, B, T, edge, boundary)
    
### REMARQUES & TASKS :
    
# Trouver transition de phase, dans la grille et les graphes

# Explorer les conditions géométriques des bords  (fermées, connectées)
# Explorer les conditions physiques aux bords (libres, fixes)

# from Metropolis import timer mais pas de import time dans le fichier_main ?
# import time, temps de calcul, + utiliser la fameuse 
# fonction de % d'avancement avec la barre
# Threading -> comprendre et imaginez une utilisation

# plt.show ou plt.savefig() et préciser les produits du code dans le rapport
# Chercher argument de plt.show qui plot 4 subplots dans une fenêtre ??
# Subplot les 2 graphes energie et magnétisation en un grand plot

# Organiser Ising_main() et le système de redirect 
# qui part de parameters_setup() et co.

# Ne pas abandonner gif_ising

# Si on fait une classe Ising_model, avec une sorte de __init__() qui fait
# le taf de Initialize_Ising_main, et toutes les autres fonctions dedans,
# est-ce qu'on ne doit plus mettre tous les arguments aux fonctions ??

# Evaluer la limite de N au-dessus de laquelle le programme
# tourne trop longtemps et restreindre le choix de N.

# Redéfinir tous les initializations de chaque fichier 
# avec le nouveau Initialize_Ising()


### QUESTIONS :

# from Metropolis import rnd_matrix, au tout début, devant l'endroit ?
# ou plutôt import Metropolis puis Metropolis.rnd_matrix ?

# from fichier.py import fonction -> mais si la fonction a besoin d'un module
# qui est lui seulement importé dans fichier.py mais pas ailleurs ?

# import os/sys

# Règle de majuscules dans les noms de variables/fonctions/fichiers

# Gestion d'exception des input : 
# utiliser logging.info/warning/error ou print ?

# if __name__ = "__main__": pour tous les fichiers mieux ??

# enlever les arguments en trop