""" 
This program is the cleaned version of Etienne_foireux.py
(with the file imports)
"""
from Metropolis import *
from Initialize import *

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

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
            from Metropolis import matrix_generator
            S_0 = matrix_generator(N, matrix_type)
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



