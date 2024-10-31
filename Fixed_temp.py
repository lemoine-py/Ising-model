
"""
This code simulates the Ising model for a fixed temperature value, defined by the user in Initialize_Ising().
"""

from Metropolis import np,ij_generate,flip_spin,local_energy,delta_E,accept_flip,total_energy,magnetic
from tqdm import tqdm
import matplotlib.pyplot as plt

def lattice_evolution(four_lattices,k_max,J,B,T):
    """ Shows 4 colored matrices showing chronological 
        states of the evolving lattice. Saves an image : <lattice_evolution.png>
    """
    fig = plt.figure()
    
    ax1 = fig.add_subplot(221)
    cax1 = ax1.matshow(four_lattices[0])
    fig.colorbar(cax1)
    plt.title(f"Iteration {1}")
    ax2 = fig.add_subplot(222)
    cax2 = ax2.matshow(four_lattices[1])
    fig.colorbar(cax2)
    plt.title(f"Iteration {int(k_max/3)}")
    ax3 = fig.add_subplot(223)
    cax3 = ax3.matshow(four_lattices[2])
    fig.colorbar(cax3)
    plt.title(f"Iteration {int(2*(k_max/3))}")
    ax4 = fig.add_subplot(224)
    cax4 = ax4.matshow(four_lattices[3])
    fig.colorbar(cax4)
    plt.title(f"Iteration {k_max}")

    plt.suptitle(f"Lattice evolution for J = {J}, B = {B}, T = {T}")
    plt.tight_layout()
    plt.savefig("lattice_evolution.png")
   
def Fix_temp_plot(energy,magnet,k_max,J,B,T):
    """ Plots the total energy and magnetization 
        of the lattice for each iteration. 
        Saves an image : <FixT_energy_magnet.png>
    """
    plt.figure(2)

    plt.subplot(121)
    plt.plot(range(int(k_max)),energy[:k_max],label = "Energy" )
    plt.legend()
    plt.grid()
    plt.xlabel("Iterations")

    plt.subplot(122)
    plt.plot(range(int(k_max)),magnet[:k_max],label = "Magnetization",color = "orange")
    plt.legend()
    plt.grid()
    plt.xlabel("Iterations")

    plt.suptitle(f"Energy and magnetization evolution for J = {J}, B = {B}, T = {T}")
    plt.tight_layout()
    plt.savefig("FixT_energy_magnet.png")


def Ising_Fix_temp(N,S_0,J,B,T,edge):
    """ Ising model simulator for one fixed temperature.
    
        Shows 4 lattice states in one plot to illustrate 
        the evolution of the system under the Metropolis iteration process.
        Shows 2 subplots for total energies and magnetizations 
        of the lattice at each point in the iteration process.
    """
    delta_e = [] # list of each energy variation after a spin flip try
    magnet = [] # list of each total magnetization of the grid
    four_lattices = [] # list of four "frames" of the grid used for plotting them
    
    k = 0 
    k_max = 15*(N**2) # Amount of tried spin flips for one temperature level
    initial_matrix = np.copy(S_0)

    with tqdm(total = k_max) as pbar: # progression bar

        while k <= k_max: 
            i, j = ij_generate(N) # Random index
            S_1 = flip_spin(i, j, S_0) # New matrix with one flipped spin
            loc_E0 = local_energy(i, j, S_0, J, B,edge) # S_0's local energy
            loc_E1 = local_energy(i, j, S_1, J, B,edge) # S_1's local energy
            dE = delta_E(loc_E0, loc_E1) # Energy difference
            S_0, flip = accept_flip(S_0,S_1,dE,T) # Validating or rejecting the flip

            if flip:
                dE_new = dE
            else:
                dE_new = 0

            delta_e.append(dE_new) # list of each new local energy change (no positive values)
            magnet.append(magnetic(S_0)) # list of each magnetization

            if k in (0,k_max/3,2*(k_max/3),k_max):
                four_lattices.append(S_0) # saving 4 "frames" in total
            k += 1
            pbar.update(1)

    #building the total energy list:
    energy = []
    i = 0
    while i < len(delta_e):
        if i == 0:
            energy.append(total_energy(initial_matrix, J, B, edge))
            #Initial total energy
        else :
            energy.append(delta_e[i]+energy[i-1])
            #Adding the new change in energy to the previous total energy
        i += 1
    
    lattice_evolution(four_lattices,k_max,J,B,T)
    Fix_temp_plot(energy,magnet,k_max,J,B,T)
    plt.show()
    

# test run
if __name__ == "__main__":
    
    from Initialize import Initialize_Ising,title,endroll
    title()
    N, matrix_type, S_0, J, B, model, T, edge = Initialize_Ising()
    # Here, matrix_type and model are not used
    Ising_Fix_temp(N, S_0, J, B, T, edge)
    endroll()

