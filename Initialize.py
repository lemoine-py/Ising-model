
""" 
This program defines all the variables that are needed 
for any Ising model simulation.
"""

from Metropolis import matrix_generator

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
            if 1 < N: # N > 1000 is not recommended
                break
            else:
                print("---> Error : please enter an integer greater than 1.")
        except ValueError:
            print("---> Error : please enter an integer greater than 1.")

    while True:
        matrix_type = input(" - Initial matrix type : random/all_up/all_down (r/u/d) ... ")
        if matrix_type in ["r","u","d"]:
            break
        else:
            print("---> Error : please choose your answer from (r/u/d).")
    S_0 = matrix_generator(N,matrix_type)

    return N, matrix_type, S_0

def parameters_setup():
    """ Asks the user for 2 inputs (returned as they are) :
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

    return J, B

def temp_model():
    """ Asks the user for 1 or 2 inputs (returned as they are) :
        model (str: "f" or "r"), if model == "f" : T (float).
        If model == "r", T = None by default.
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
    print("* \"Torus shaped\" lattice (t): opposite edges are connected to each other. All spins have 4 neighbours.")
    while True:
        edge = input("*** [c/t] ... ")
        if edge == "c" or edge == "t":
            break
        else:
            print("---> Error : please choose your answer from (c/t).")    
    return edge

### Main initializing function (all together)
def Initialize_Ising():
    """ Initialization of the whole Ising model.
        Returns :
            N (int), matrix_type (str), S_0 (numpy.ndarray), 
            J (float), B (float), model (str), T (float), edge (str).
    """
    print(" ------ Initialization of the Ising_model ------ \n")
    N,matrix_type, S_0 = init_lattice()
    J,B = parameters_setup()
    model,T = temp_model()
    edge = edge_condition()
    print("\n ------ Starting the simulation ------ \n")

    return N, matrix_type, S_0, J, B, model, T, edge

def endroll():
    print("\n ============= Simulation ended ============= \n")

# test run
if __name__ == "__main__":
    N, matrix_type, S_0, J, B, model, T, edge = Initialize_Ising()