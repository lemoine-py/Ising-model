"""
This program plots the final energies and magnetizations of each lattice for each temperature in a certain range.
"""

from prototype_ising import *

def Range_temp_title():
    print("\n ====== Range_temp.py ====== \n")
    
def Ising_Range_temp_plot() :
    
    plt.figure(5) # plt.figure(1 to 4) are already taken by the 4 lattice plots in prototype_ising.py
    plt.subplot(111)
  
    plt.plot(range(0,50),energy[:50],label = "Energie" )
    plt.legend()
    plt.grid()
    plt.title(f"Energie finale selon T, avec B = {B}, J = {J}")
    plt.xlabel("Température")
    plt.ylabel("Energie")
    #plt.savefig("Energy_T.png")
    plt.show
  
    plt.figure(6)
    plt.subplot(111)
  
    plt.plot(range(0,50),magnetization[:50],label = "Magnétisation",color = "red")
    plt.legend()
    plt.grid()
    plt.title(f"Magnétisation finale selon T, avec B = {B}, J = {J}")
    plt.xlabel("Température")
    plt.ylabel("Magnétisation")
    #plt.savefig("Magnet_T.png")
    plt.show
    
    
def Ising_Range_temp():
    """Ising model simulator for a range of temperature.
    Plots of total final energy and magnetization of the lattice."""
    
    Ising_Range_temp_title()
    N,J,B,_ = parameters_setup()
    
    magnetization = []
    energy =[]
    
    T = 0.1
    T_f = 10
    T_step = 0.1
    
    while T < T_f:
        k = 0
        k_max = 6*(N**2)
        S_0 = rnd_matrix(N) # Starting with a random lattice for each temperature
        
        while k < k_max: # Trying 6n flips for one temperature level
            i, j = ij_generate(N) # Random index
            S_1 = flip_spin(i, j, S_0) # New matrix with one flipped spin
            loc_E0 = local_energy(i, j, S_0, B, J) # S_0's local energy
            loc_E1 = local_energy(i, j, S_1, B, J) # S_1's local energy
            dE = delta_E(loc_E0, loc_E1) # Energy difference
            S_0, flip = accept_flip(S_0,S_1, dE, T) # Validating or rejecting the flip
            k += 1
            
        energy.append(total_energy(S_0,B,J))
        magnetization.append(magnetic(S_0))
        T += T_step
  
    Ising_range_temp_plot(energy,magnetization)

# If only one plot with two subplots is needed, 
# use only once 'plt.figure(5)'' then 'plt.subplot(211)''
# then twice 'plt.plot(...)'


### Calling functions

if __name__ == "__main__":
    Ising_Range_temp_title()
    
    Ising_Range_temp()