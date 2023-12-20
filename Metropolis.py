
"""
This program contains the basic functions for the Metropolis algorithm.
"""

import numpy as np

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
    matrix = np.ones((N,N)) # If a "down_matrix" is needed, multiply by -1.
    return matrix

def matrix_generator(N,matrix_type):
    """ Generates and returns a matrix following matrix_type. """
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

### Magnetization calculator
def magnetic(S_0):
    """Magnetization (sum of all spin values) of the given lattice"""
    magnet = np.sum(S_0)
    return magnet

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

### Metropolis algorithm (for one temperature level) :
def Metropolis(N, S_0, J, B, T, edge): 
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
    return S_0


# test run
if __name__ == "__main__":
    from Initialize import Initialize_Ising
    N,matrix_type,S_0,J,B,model,T,edge = Initialize_Ising()
    # Here, matrix_type and model are not used
    Metropolis(N,S_0,J,B,T,edge)


