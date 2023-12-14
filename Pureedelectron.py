""" 
Mashed electrons.
Goddamn Etienne, you can't imagine how much I worked to clean all this mess in your code.
And yes it is important to have a clean code.
You just have to run this code and you'll see.

By the way, the names of the two subplots are too long, they're hiding each other on the plot.
"""

import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

### Initial configuration :
def rnd_matrix(N):
    """ Generates a NxN matrix with randomly up or down spins.
        Argument : N (positive integer)
        Return : NxN spin matrix  (-1 or +1)
    """
    spins = (1,-1)
    matrix = np.random.choice(spins,size=(N,N))
    return matrix

def up_matrix(N):
    """ Generates a NxN matrix only with up spins. """
    matrix = np.ones((N,N))
    return matrix
# Just multiply up_matrix by -1 if a "down_matrix" is needed.


### Spin modification :
def ij_generate(N):
    """ Randomly generates two numbers, used later to access a random spin. """
    i,j = tuple(np.random.randint(N,size=2))
    return i,j

def flip_spin(i,j,S_0):
    """ Flips a random spin in the given matrix. """
    S_1 = np.copy(S_0)
    S_1[i][j] *= -1
    return S_1


### Energy calculator :
def local_energy_J(i,j,S_0,J,edge):
    """ Local energy due to coupling J """
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
    """ Local energy due to magnetic field B """
    loc_energy_B = 0
    loc_energy_B -= B*S_0[i][j]
    return loc_energy_B

def local_energy(i,j,S_0,J,B,edge):
    """ Sum of the two local energies.
        Arguments : i (integer), j (integer), S_0 (matrix), J (float), B (float)
        Return : float 
    """
    return local_energy_J(i,j,S_0,J,edge) + local_energy_B(i,j,S_0,B)

def total_energy(S_0,J,B,edge):
    """ Returns the total energy of the entire lattice. """
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
    """ Returns the energy difference after a spin flip. """
    dE = loc_E_1 - loc_E_0
    return dE

### Accepting or rejecting the spin modification:
def accept_flip(S_0,S_1,dE,T):
    """ Accepts or rejects the random spin flip, based on delta_E and T.
        Arguments: S_0 (matrix), delta_E (float), T (float)
        Return: S_0 (modified matrix), flip (boolean)
    """ 
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



###### Other utilities :

### Magnetization calculator
def magnetic(S_0):
    """Magnetization (sum of all spin values) of the given lattice"""
    magnet = sum(sum(S_0))
    return magnet

### Program's end message :
def endroll():
    print("\n =============== END =============== \n")

### Timer decorator  :
def timer(function):
    def timed_function(*args, **kwargs):
        t_start = time.perf_counter()
        out = function(*args, **kwargs)
        print(f" --- Total time : {time.perf_counter() - t_start:.2f} seconds")
        return out
    return timed_function
  
def matrix_generator(N,matrix_type):
    if matrix_type == "r":
        S_0 = rnd_matrix(N)
    elif matrix_type == "u":
        S_0 = up_matrix(N)
    elif matrix_type == "d":
        S_0 = - up_matrix(N)
    return S_0

""" The following program defines the 'global variables'
     used for the Ising model simulation.
"""

def title():
    """ Prints the program's title """
    print("\n =============== ISING MODEL =============== ")
    print(" --- Simulation for spin interactions")
    print(" --- in a 2D lattice, using the Ising model.\n")

def init_lattice():
    """ Asks the user for 2 inputs :
        N (int > 1), matrix_type (str: "r" or "u" or "d").
        Generates the lattice according to its type.
        Returns the lattice's size (N) and the lattice's matrix of spin values (S_0)
    """
    print(" --- Electron lattice --- \n")

    while True:
        N = input(" - Matrix size : N = ... ") 
        try:
            N = int(N) 
            if 2 <= N <= 500: # What's the max N ??
                break
            else:
                print("---> Error : please enter an integer between 1 and 500.")
        except ValueError:
            print("---> Error : please enter an integer between 1 and 500.")

    while True:
        matrix_type = input(" - Initial matrix type : random/all_up/all_down (r/u/d) ... ")
        if matrix_type == "r":
            S_0 = rnd_matrix(N)
            break
        elif matrix_type == "u":
            S_0 = up_matrix(N)
            break
        elif matrix_type == "d":
            S_0 = - up_matrix(N) 
            break
        else:
            print("---> Error : please choose your answer from (r/u/d).")

    return N, matrix_type, S_0

def parameters_setup():
    """ Asks the user for 2 inputs (that are then returned as they are) :
        J (float), B (float).
    """
    print("\n --- Physical parameters --- \n")
    while True:
        J = input(" - Spin coupling interaction : J = ... ")
        try:
            J = float(J)
            break
        except ValueError:
            print("---> Error : please enter a float.")
    while True:
        B = input(" - External magnetic field value : B = ... ")
        try:
            B = float(B)
            break
        except ValueError:
            print("---> Error : please enter a float.")

    # Same exception handling for the two -> is there a way to combine ?
    return J, B

def temp_model():
    """ Asks the user for 1 input :
        model (str: "f" or "r").
    """
    print("\n --- Simulation type --- \n")
    print("* Fixed_T (f): Evolution of the lattice over time for a fixed temperature")
    print("* Ranged_T (r): Final Energies and magnetizations for a range of temperatures")
    while True:
        model = input("*** [f/r] ... ")
        if model == "f":
            while True:
                T = input(" - System's temperature : T = ... ")
                try:
                    T = float(T)
                    break
                except ValueError:
                    print("---> Error : please enter a float.")
            break
        elif model == "r":
            T = None
            break
        else:
            print("---> Error : please choose your answer from (f/r).")
    return model,T

def edge_condition():
    """ Asks the user for 1 input (that is then returned as it is) :
        edge (str: "c" or "t").
    """
    print("\n --- Edge conditions --- \n")
    print("* \"Closed square\" lattice (c): edge spins have 3 neighbours and hook spins have 2.")
    print("* \"Torus shaped\" lattice (t) : opposite edges are connected to each other. All spins have 4 neighbours.")
    while True:
        edge = input("*** [c/t] ... ")
        if edge == "c" or edge == "t":
            break
        else:
            print("---> Error : please choose your answer from (c/t).")    
    return edge

def boundary_condition():
    """ Asks the user for 1 input (that is then returned as it is) :
        boundary (str: "n" or "d").
    """
    print("\n --- Boundary conditions --- \n")
    print("* No conditions (n): edge spins free to flip.")
    print("* \"Dirichlet\" condition (d): edge spins fixed in a permanent state.")
    while True:
        boundary = input("*** [n/d] ... ")
        if boundary == "n" or boundary == "d": # can I write "if b == n or d" ??
            break
        else:
            print("---> Error : please choose your answer from (n/d).")
    return boundary

def Initialize_Ising():
    """ Initialization of the whole Ising model.
        Returns :
            N (int),S_0 (numpy.ndarray), J (float), B (float),
            model (str), T (float), edge (str), boundary (str)"""
    title()
    print(" ------ Initialization of the Ising_model ------ \n")
    N,matrix_type, S_0 = init_lattice()
    J,B = parameters_setup()
    model,T = temp_model()
    edge = edge_condition()
    boundary = boundary_condition()
    print("\n ------ Starting the simulation ------ \n")
    return N, matrix_type, S_0, J, B, model, T, edge, boundary

def foireux_start():
    print("\n ====== Foireux program ====== \n")
    N, matrix_type, S_0, J, B, model, T, edge, boundary = Initialize_Ising()

    return N, matrix_type, S_0, J, B, model, T, edge, boundary

def Ising_Range_temp(N, matrix_type, S_0, J, B, model, T, edge, boundary):
    """ Ising model simulator for a range of temperature.
        Plots total final energy and magnetization of the lattice for each temperature.
    """
    magnetisation = []
    energy = []

    T = 0.1  # Initial temperature
    temp_steps = 100  # Amount of steps in the temperature range
    with tqdm(total=temp_steps) as pbar: # progression bar
        while T < 10:
            k = 0
            k_max = 15 * (N ** 2) # Amount of Metropolis iterations for one temperature level

            S_0 = matrix_generator(N, matrix_type)

            while k <= k_max:  # Flipping spins 15n times for one temperature level
                i, j = ij_generate(N) # Random index
                S_1 = flip_spin(i, j, S_0) # New matrix with one flipped spin
                loc_E0 = local_energy(i, j, S_0, B, J, edge) # S_0's local energy
                loc_E1 = local_energy(i, j, S_1, B, J, edge) # S_1's local energy
                dE = delta_E(loc_E0, loc_E1) # Energy difference
                S_0, flip = accept_flip(S_0, S_1, dE, T) # Validating or rejecting the flip
                k += 1
            energy.append(total_energy(S_0, J, B, edge))
            magnetisation.append(magnetic(S_0))
            T += 0.1
            pbar.update(1)  # Met à jour la barre de progression

    # Vos tracés restent inchangés
    plt.figure(5)
    plt.subplot(111)
    plt.plot(range(temp_steps), energy, label="Energie")
    plt.legend()
    plt.title(f"Energie finale selon T, avec B = {B}, J = {J}")
    plt.xlabel("Température")
    plt.ylabel("Energie")

    plt.figure(6)
    plt.subplot(111)
    plt.plot(range(temp_steps = 100), magnetisation, label="Magnétisation", color="orange")
    plt.legend()
    plt.title(f"Magnétisation finale selon T, avec B = {B}, J = {J}")
    plt.xlabel("Température")
    plt.ylabel("Magnétisation")

    plt.show()  # Affiche les graphiques à la fin de l'exécution de la fonction

    #plt.savefig("Magnet_T.png")

# If only one plot with two subplots is needed,
# use only once 'plt.figure(5)'' then 'plt.subplot(211)''
# then twice 'plt.plot(...)'


def Ising_Fixed_temp(N, matrix_type, S_0, J, B, model, T, edge, boundary):
    """ Ising model simulator for a range of temperature (0-5).
        Shows 2 plots for total final energies and magnetizations 
        of the lattice for each temperature.
    """
    delta_e = []
    magnet = []
    k = 0 
    k_max = 15*(N**2) # Amount of Metropolis iterations for one temperature level
    initial_matrix = np.copy(S_0)

    with tqdm(total = k_max) as pbar: # progression bar

        while k <= k_max: 
            i, j = ij_generate(N) # Random index
            S_1 = flip_spin(i, j, S_0) # New matrix with one flipped spin
            loc_E0 = local_energy(i, j, S_0, J, B,edge) # S_0's local energy
            loc_E1 = local_energy(i, j, S_1, J, B,edge) # S_1's local energy
            dE = delta_E(loc_E0, loc_E1) # Energy difference
            S_0, flip = accept_flip(S_0,S_1, dE, T) # Validating or rejecting the flip
            if k == 0 or k== k_max/3 or k == 2*(k_max/3) or k == k_max:
                fig = plt.figure()
                ax = fig.add_subplot(111)
                cax = ax.matshow(S_0)
                fig.colorbar(cax)
                plt.title(f"Etat de la matrice après {k} itérations avec B = {B}, J = {J}, et T = {T} ")
                plt.show()
            if flip:
                dE_new = dE
            else:
                dE_new = 0
            delta_e.append(dE_new)
            magnet.append(magnetic(S_0))
            k += 1
            pbar.update(1)
    energy = []
    i = 0
    while i < len(delta_e):
        if i == 0:
            energy.append(total_energy(initial_matrix, J, B, edge))
        else :
            energy.append(delta_e[i]+energy[i-1])
        i += 1

    plt.figure(1)
    plt.subplot(121)

    plt.plot(range(0,15*(N**2)),energy[:15*(N**2)],label = "Energie" )
    plt.legend()
    plt.grid()
    plt.title(f"Energie selon le nombre d'itérations, avec B = {B}, J = {J} et T = {T}")
    plt.xlabel("Itérations")
    plt.ylabel("Energie")
    #plt.savefig("Energy_FixT.png")

    #plt.figure(2)
    plt.subplot(122)
    plt.plot(range(0,15*(N**2)),magnet[:15*(N**2)],label = "Magnétisation",color = "orange")
    plt.legend()
    plt.grid()
    plt.title(f"Magnétisation selon le nombre d'itérations, avec B = {B}, J = {J} et T = {T}")
    plt.xlabel("Itérations")
    plt.ylabel("Magnétisation")
    #plt.savefig("Magnet_FixT.png")

    plt.show()

### Calling functions

N, matrix_type, S_0, J, B, model, T, edge, boundary = foireux_start()

if model == "f":
    Ising_Fixed_temp(N, matrix_type, S_0, J, B, model, T, edge, boundary)
elif model == "r":
    Ising_Range_temp(N, matrix_type, S_0, J, B, model, T, edge, boundary)

endroll()
