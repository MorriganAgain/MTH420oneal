# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Finian O'Neal>
<MTH 420>
<5/1/25>
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.normal(size=[n, n])
    mean = np.mean(A, axis=1)
    return np.var(mean)

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    
    n = np.linspace(100, 1000, 10, dtype=int)
    n_vars = []
    for i in n:
        n_vars.append(var_of_means(i))
    
    fig, axs = plt.subplots()
    axs.plot(n, n_vars)
    plt.show()
    


# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    fig, axs = plt.subplots()
    axs.plot(x, np.sin(x))
    axs.plot(x, np.cos(x))
    axs.plot(x, np.arctan(x))
    plt.show()



# Problem 3

def func3(x):
    return 1 / (x-1)

def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2, 1, 100)
    x2 = np.linspace(1, 6, 100)
    fig, axs = plt.subplots()
    axs.plot(x1, func3(x1), linestyle='--',linewidth=4, color='m')
    axs.plot(x2, func3(x2), linestyle='--',linewidth=4, color='m')
    plt.show()
    


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    fig, axs = plt.subplots(2, 2)
    x = np.linspace(0, 2 * np.pi)
    
    axs[0][0].plot(x, np.sin(x), "g")
    axs[0][0].set_ylim([-2, 2])
    axs[0][0].set_xlim([0, 2 * np.pi])
    axs[0][0].set_title("Sin(x)")
    axs[0][1].plot(x, np.sin(2*x), "r--")
    axs[0][1].set_ylim([-2, 2])
    axs[0][1].set_xlim([0, 2 * np.pi])
    axs[0][1].set_title("Sin(2x)")
    axs[1][0].plot(x, 2*np.sin(x), "b--")
    axs[1][0].set_ylim([-2, 2])
    axs[1][0].set_xlim([0, 2 * np.pi])
    axs[1][0].set_title("2Sin(x)")
    axs[1][1].plot(x, 2*np.sin(2*x), "m.")
    axs[1][1].set_ylim([-2, 2])
    axs[1][1].set_xlim([0, 2 * np.pi])
    axs[1][1].set_title("2Sin(2x)")
    plt.title("Problem 4 Graphs")
    plt.show()
    


# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    data = np.load("MatplotlibIntro/FARS.npy")
    fig, axs = plt.subplots(1, 2)
    axs[0].scatter(data[:,1], data[:,2], marker=".", color="black", s=0.1)
    axs[0].set_aspect("equal")
    axs[0].set_xlabel("Longitude")
    axs[0].set_ylabel("Latitude")

    axs[1].hist(data[:,0], bins=np.arange(0, 24))
    axs[1].set_xlim(0, 23)
    axs[1].set_xlabel("Hour")
    axs[1].set_ylabel("Fatalities")
    plt.show()

# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    x, y = np.linspace(-2*np.pi, 2*np.pi, 100), np.linspace(-2*np.pi, 2*np.pi, 100)
    X, Y = np.meshgrid(x, y)
    z = (np.sin(X) * np.sin(Y)) / (X * Y)
    plt.subplot(121)
    plt.pcolormesh(X, Y, z, cmap="viridis", shading="auto")
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    
    plt.subplot(122)
    plt.contour(X, Y, z, 10, cmap="magma")
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    plt.show()

if __name__ == "__main__":
    prob6()