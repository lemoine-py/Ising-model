"""
Code pour une simulation Ising avec T fixé dans parameters_setup()
"""

from Metropolis import *

def Ising_Fixed_temp_title():
    print("\n ====== Fixed_temp.py ====== \n")
    
    
### Lattice visualisation
def lattice_visualize(S_0,k,N):
  """ Plots 4 lattice states with matshow and colorbar """
  if k == 0 or k == 2*(N**2) or k == 4*(N**2) or k == 6*(N**2):
      fig, ax = plt.subplots()
      cax = ax.matshow(S_0)
      fig.colorbar(cax)
      ax.set(title=f't = {k}', ylabel="Coordonnées de la grille")



  
#Ising_simulate()
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
def Ising_Fixed_temp():
    """ Simulation of the Ising model 
    for the constants defined in parameters_setup() by the user."""

    title()
    N,J,B,T = parameters_setup()
    S_0 = rnd_matrix(N) 
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
 

if __name__ == "__main__":
    Ising_Fixed_temp_title()
    
    Ising_Fixed_temp()