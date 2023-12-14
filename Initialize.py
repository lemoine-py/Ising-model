""" This program defines the 'global variables'
     used for the Ising model simulation.
"""

from Metropolis import rnd_matrix,up_matrix
 
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


if __name__ == "__main__":
    N, matrix_type, S_0, J, B, model, T, edge, boundary = Initialize_Ising()