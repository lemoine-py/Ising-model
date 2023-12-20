
"""
Code pour une simulation Ising avec T fixé dans Initialize_Ising()
"""

from Metropolis import *
from tqdm import tqdm
import matplotlib.pyplot as plt
    
### Lattice visualisation
def lattice_visualize(S_0,k,k_max,J,B,T):
    """ Plots 4 lattice states with matshow and colorbar """
    if k in (0,k_max/3,2*(k_max/3),k_max):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(S_0)
        fig.colorbar(cax)
        plt.title(f"Iteration {int(k)} with J = {J}, B = {B}, T = {T}")
        plt.show()
        
def four_visuals(four_lattices,k_max):     
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    cax1 = ax1.matshow(four_lattices[0])
    fig.colorbar(cax1)
    plt.title(f"Iteration {1}")
    ax2 = fig.add_subplot(222)
    cax2 = ax2.matshow(four_lattices[1])
    fig.colorbar(cax2)
    plt.title(f"Iteration {k_max/3}")
    ax3 = fig.add_subplot(223)
    cax3 = ax3.matshow(four_lattices[2])
    fig.colorbar(cax3)
    plt.title(f"Iteration {2*(k_max/3)}")
    ax4 = fig.add_subplot(224)
    cax4 = ax4.matshow(four_lattices[3])
    fig.colorbar(cax4)
    plt.title(f"Iteration {k_max}")
    fig.tight_layout()
    plt.suptitle(f"J = {J}, B = {B}, T = {T}")
    plt.show()
    


### Lattice animation
def lattice_animate(all_lattices,J,B,T):
    """ Shows and clears continuously each different lattice state 
        evolving over time.
        Caution: the function doesn't save anything as a file and
        it couldn't do such thing.
    """
    fig, ax = plt.subplots()
    for i, i_lattice in enumerate(all_lattices):
        ax.clear()
        ax.imshow(i_lattice)
        ax.set_title(f" Flip {i} with J = {J}, B = {B}, T = {T}")
        plt.pause(0.0000001)


def Ising_Fixed_temp(N,matrix_type,S_0,J,B,model,T,edge):
    """ Ising model simulator for one fixed temperature.
        Shows 2 subplots for total energies and magnetizations 
        of the lattice at each point in the iteration process
        Shows an animation for the evolution of the lattice.
    """
    delta_e = []
    magnet = []
    four_lattices = []
    all_lattices = []

    k = 0 
    k_max = 15*(N**2) # Amount of Metropolis iterations for one temperature level
    initial_matrix = np.copy(S_0) # Why ? when i=1 then S_0, line 79

    with tqdm(total = k_max) as pbar: # progression bar

        while k <= k_max: 
            i, j = ij_generate(N) # Random index
            S_1 = flip_spin(i, j, S_0) # New matrix with one flipped spin
            loc_E0 = local_energy(i, j, S_0, J, B,edge) # S_0's local energy
            loc_E1 = local_energy(i, j, S_1, J, B,edge) # S_1's local energy
            dE = delta_E(loc_E0, loc_E1) # Energy difference
            S_0, flip = accept_flip(S_0,S_1,dE,T) # Validating or rejecting the flip
            
            lattice_visualize(S_0,k,k_max,J,B,T)
                
            if flip:
                dE_new = dE
                all_lattices.append(S_0)
            else:
                dE_new = 0

            if k in (0,k_max/3,2*(k_max/3),k_max):
                four_lattices.append(S_0)
            if k%((N**2)*0.05) == 0:
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
    
    fig12 = plt.figure(1)
    plt.subplot(121)

    plt.plot(range(300),energy[:-1],label = "Energie" )
    plt.legend()
    plt.grid()
    plt.title(f"J = {J}, B = {B}, T = {T}")
    plt.xlabel("Steps")
    #plt.savefig("Energy_FixT.png")

    plt.subplot(122)
    plt.plot(range(300),magnet[:-1],label = "Magnétisation",color = "orange")
    plt.legend()
    plt.grid()
    plt.title(f"J = {J}, B = {B}, T = {T}")
    plt.xlabel("Steps")
    #plt.savefig("Magnet_FixT.png")
    plt.tight_layout()
    plt.show()
    four_visuals(four_lattices,k_max)
    #lattice_animate(all_lattices,J,B,T)

if __name__ == "__main__":
    
    from Initialize import Initialize_Ising
    N, matrix_type, S_0, J, B, model, T, edge = Initialize_Ising()
    Ising_Fixed_temp(N, matrix_type, S_0, J, B, model, T, edge)