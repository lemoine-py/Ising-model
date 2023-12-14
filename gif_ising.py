
"""
Pareil que prototype.py mais montre une animation noir et blanc en format .gif
de l'évolution de la grille pour des paramètres fixés.
"""
from prototype_ising import *
import imageio
from matplotlib.animation import FuncAnimation

def plot_lattice_gif(S_0):
    """Creates an image for the current lattice state"""
    plt.imshow(S_0, cmap='hot', interpolation='nearest')
    plt.title('Spins lattice')
    plt.axis('off')  # Désactiver les axes pour une meilleure apparence
    plt.close()
    return plt.gcf()  # Retourne la figure pour l'animation

images = []

### Simple Ising simulation
def Ising_simulate_gif():
    """Simulation of the Ising model for the constants defined in parameters_setup()."""

    title()
    N,J,B,T = parameters_setup()
    S_0 = rnd_matrix(N)
    logging.info("S_0:\n",S_0)

    k=0
    while k < 6*(N**2): # Flipping spins 6n times for the given Temperature
        i, j = ij_generate(N) # Random index
        S_1 = flip_spin(i,j,S_0) # New matrix with one flipped spin
        loc_E0 = local_energy(i, j, S_0, B, J) # S_0's local energy
        loc_E1 = local_energy(i, j, S_1, B, J) # S_1's local energy
        dE = delta_E(loc_E0, loc_E1) # Energy difference
        S_0, flip = accept_flip(S_0,S_1,dE,T) # Validating or rejecting the flip
        if flip:
            image = plot_lattice_gif(S_0)  # Creates one frame for the current lattice state
            images.append(image) # Adds the frame to the list of frames
        k += 1
    imageio.mimsave('ising_animation1.gif', images, duration=0.001) # Saves the animation into a .gif file

#Ising_simulate_gif()

def plot_ising_model(S):
    plt.imshow(S, cmap='hot', interpolation='nearest')
    plt.title('Ising Model')
    plt.axis('off')

def Ising_simulate_gify():
    """Simulation of the Ising model for the constants defined in parameters_setup()."""

    title()
    N,J,B,T = parameters_setup()
    S_0 = rnd_matrix(N)
    logging.info("S_0:\n",S_0)

    # Création d'une liste pour stocker les tracés successifs
    plots = []

    k = 0
    while k < 6*(N**2):  # Flipping spins 6n times for the given Temperature
        i, j = ij_generate(N)  # Random index
        S_1 = flip_spin(i, j, S_0)  # New matrix with one flipped spin
        loc_E0 = local_energy(i, j, S_0, B, J)  # S_0's local energy
        loc_E1 = local_energy(i, j, S_1, B, J)  # S_1's local energy
        dE = delta_E(loc_E0, loc_E1)  # Energy difference
        S_0, flip = accept_flip(S_0, S_1, dE, T)  # Validating or rejecting the flip

        # Ajout du tracé actuel à la liste
        plt.figure()
        plot_ising_model(S_0)
        plt.close()
        plots.append(plt.gcf())

        k += 1

    # Sauvegarde de l'animation au format GIF
    imageio.mimsave('ising_animation11.gif', plots, duration=0.01)
    
Ising_simulate_gify()


def metropolis(S_0,N,J,B,T):
    i, j = ij_generate(N) # Random index
    S_1 = flip_spin(i,j,S_0) # New matrix with one flipped spin
    loc_E0 = local_energy(i, j, S_0, B, J) # S_0's local energy
    loc_E1 = local_energy(i, j, S_1, B, J) # S_1's local energy
    dE = delta_E(loc_E0, loc_E1) # Energy difference
    S_0, flip = accept_flip(S_0,S_1,dE,T)
    return S_0

def animate(frame):
    global current_S_0
    plt.clf()
    current_S_0 =  metropolis(current_S_0,N,J,B,T)
    plt.imshow(S_0, cmap='hot', interpolation='nearest')
    plt.title('Ising Model - Frame {}'.format(frame))
    plt.axis('off')
"""    
title()
N,J,B,T = parameters_setup()
S_0 = rnd_matrix(N) 

current_S_0 = S_0

steps = 3*(N**2)
animation = FuncAnimation(plt.gcf(), animate, frames=steps, interval=100, repeat=False)
animation.save('ising_animation.gif', writer='imagemagick', fps=50)
"""