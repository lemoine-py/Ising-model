"""
Free coding space
It can be "foireux"
"""

from Metropolis import *
import matplotlib.ticker as mticker

def foireux_start():
    print("\n ====== Foireux program ====== \n")
    N,J,B,T = parameters_setup()
    S_0 = rnd_matrix(N)
    return N,J,B,S_0

def Ising_Temp_range(N,J,B,S_0):
    """Ising model simulator for a range of temperature (0-5).
    Plots of total final energy and magnetization of the lattice."""
    magnetization = []
    energy =[]

    T = 0.1 # Initial temperature
    while T < 5:
        k = 0
        k_max = 6*(N**2)
        S_0 = rnd_matrix(N) # Starting with a random lattice for each temperature
        while k < k_max: # Flipping spins 6n times for one temperature level
  
            i, j = ij_generate(N) # Random index
            S_1 = flip_spin(i, j, S_0) # New matrix with one flipped spin
            loc_E0 = local_energy(i, j, S_0, B, J) # S_0's local energy
            loc_E1 = local_energy(i, j, S_1, B, J) # S_1's local energy
            dE = delta_E(loc_E0, loc_E1) # Energy difference
            S_0, flip = accept_flip(S_0,S_1, dE, T) # Validating or rejecting the flip
            k += 1
        energy.append(total_energy(S_0,B,J))
        magnetization.append(magnetic(S_0))
        T += 0.1
    """
    fig, (ax1,ax2) = plt.subplots(2,1)
    ax1.plot(range(0,50),energy[:50],label = "Energie")
    ax1.legend()
    ax1.grid()
    ax1.set_title("Energie finale")
    ax1.xlabel("Température")
    ax1.ylabel("Energie")
    ax2.plot(range(0,50),magnetization[:50],label = "Magnétisation",color = "red")
    ax2.legend()
    ax2.grid()
    ax2.set_title("Magnétisation finale")
    ax2.sharex(ax1)
    ax2.ylabel("Magnétisation")
    fig.tight_layout()
    """
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))  # define the figure and subplots
    axes = axes.ravel()  # array to 1D
    data_y = [energy,magnetization]
    labels = ["Energie","Magnétisation"] # list of labels for each subplot
    colors = ['tab:blue', 'tab:orange']  # list of colors for each subplot
    
    for data,label,color,ax in zip(data_y,labels,colors,axes):
        plt.plot(x=T/0.1,y=data, ax=ax, color=color, label=label, title="Test")
        ax.legend()
        ax.grid()

    fig.tight_layout()
    plt.show()
 
#N,J,B,S_0 = foireux_start()
    
#energy_magnet_simulate(N,J,B,S_0)

# If only one plot with two subplots is needed, 
# use only once 'plt.figure(5)'' then 'plt.subplot(211)''
# then twice 'plt.plot(...)'


### Matrix visualizer for the lattice
def lattice_photos(S_0,k,N,four_lattices):
    if k == 0 or k == 2*(N**2) or k == 4*(N**2) or k == 6*(N**2):
        four_lattices.append(np.copy(S_0))
    return four_lattices
        
def lattice_visualize(four_lattices):
    fig, axes = plt.subplots(2,2)
    for i,ax in enumerate(axes):
        cax = ax.matshow(four_lattices[i])
        fig.colorbar(cax)
        ax.set(title=f't = {k}', ylabel="Coordonnées de la grille")
        figure()
        
    for i in range(4):
        plt.subplots(2, 2, i)
        plt.matshow(four_lattices[i])
        plt.colorbar()
    
def lattice_visual(photos):
    fig, axes = plt.subplots(2,2)
    for ax in axes:
        
        cax = ax.imshow(photos, vmin=-1, vmax=1, cmap='coolwarm')
        ax.set_title(f'Configuration de la grille en t={k}')
        cbar = fig.colorbar(cax, ticks=[-1, 0, 1],
                            format=mticker.FixedFormatter(['-1', '+1']), extend='both')
        labels = cbar.ax.get_yticklabels()
        labels[0].set_verticalalignment('top')
        labels[-1].set_verticalalignment('bottom')
        
def lattice_animate(all_lattices):
    """Shows and clears continuously each different lattice state evolving over time.
        Caution: the function doesn't save anything as a file and it couldn't do such thing.
    """
    fig, ax = plt.subplots()
    for i, i_lattice in enumerate(all_lattices):
        ax.clear()
        ax.imshow(i_lattice)
        ax.set_title(f"Configuration à l'itération {i}")
        # Note that using time.sleep does *not* work here!
        plt.pause(0.000001)
        
### Simple Ising simulation
def Ising_simulate():
    """ Simulation of the Ising model 
    for the constants defined in parameters_setup() by the user."""

    title()
    N,J,B,T = parameters_setup()
    S_0 = rnd_matrix(N) 
    lattice_data = [] #
    all_lattices = [] 
    k=0
    while k <= 6*(N**2): # Trying 6n flips for the given temperature
        
        i, j = ij_generate(N) # Random index
        S_1 = flip_spin(i,j,S_0) # New matrix with one flipped spin
        loc_E0 = local_energy(i, j, S_0, B, J) # S_0's local energy
        loc_E1 = local_energy(i, j, S_1, B, J) # S_1's local energy
        dE = delta_E(loc_E0, loc_E1) # Energy difference
        S_0, flip = accept_flip(S_0,S_1,dE,T) # Validating or rejecting the flip
        if flip:
            all_lattices.append(S_0) # So that identical lattices aren't animated
        k+=1 
    lattice_animate(all_lattices)
    #plt.show()
 

Ising_simulate()

