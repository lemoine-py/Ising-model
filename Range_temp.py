
"""
This program plots the final energies and magnetizations 
of each lattice for each temperature in a certain range.
"""

from Metropolis import np,matrix_generator,Metropolis,total_energy,magnetic
from tqdm import tqdm
import matplotlib.pyplot as plt

def Range_temp_plot(range_energy,range_magnet):
    """ Plots the final total energies and magnetizations for each temperature.
        Saves an image : <RangeT_energy_magnet.png>.
    """
    plt.figure()
    
    plt.subplot(121)
    plt.plot(np.arange(0.1,10.1,0.1), range_energy, label="Energies")
    plt.legend()
    plt.xlabel("Temperature")

    plt.subplot(122)
    plt.plot(np.arange(0.1,10.1,0.1), range_magnet, label="Magnetizations", color="orange")
    plt.legend()
    plt.xlabel("Temperature")

    plt.suptitle(f"Final states of a lattice under J = {J}, B = {B}")
    plt.tight_layout()
    plt.savefig("RangeT_energy_magnet.png")
    plt.show()
    
    
def Ising_Range_temp(N, matrix_type, J, B, edge):
    """ Ising model simulator for a range of temperature.
        Plots total final energy and magnetization of the lattice for each temperature.
    """
    range_magnet = []
    range_energy = []

    T = 0.1  # Initial temperature
    temp_steps = 100
    with tqdm(total=temp_steps) as pbar: # Progression bar
        while T < 10:
            S_0 = matrix_generator(N, matrix_type) #New start matrix for each T
            S_0 = Metropolis(N,S_0,J,B,T,edge)
            range_energy.append(total_energy(S_0,J,B,edge))
            range_magnet.append(magnetic(S_0))
            T += 0.1
            pbar.update(1)  # Updates the progression bar
            
    Range_temp_plot(range_energy,range_magnet)

# test run
if __name__ == "__main__":

    from Initialize import Initialize_Ising
    N, matrix_type, S_0, J, B, model, T, edge = Initialize_Ising()
    # Here, model is not used.
    Ising_Range_temp(N, matrix_type, J, B, edge)
