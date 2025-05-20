# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Finian O'Neal>
<MTH 420>
<5/19/25>
"""

import numpy as np
from cmath import sqrt
from scipy import linalg as la
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    
    Q, R = la.qr(A, mode='economic')
    return la.solve_triangular(R, Q.T @ b)
    

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    
    data = np.load("LeastSquares_Eigenvalues/housing.npy")
    m, n = np.shape(data)
    A = np.ones([m, n])
    x = data[:, 0]
    y = data[:, 1]
    A[:, 0] = x
    b = data[:, 1]
    fit = least_squares(A, b)
    y_fit = x * fit[0] + fit[1]
    
    fig, axs = plt.subplots()
    axs.scatter(x, y)
    axs.plot(x, y_fit)
    
    plt.show()


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    
    data = np.load("LeastSquares_Eigenvalues/housing.npy")
    x, y = data[:, 0], data[:, 1]
    x_smooth = np.linspace(x[0], x[-1], 1000)
    
    fig, axs = plt.subplots(4)
    
    degrees = [3, 6, 9, 12]
    
    for i, degree in enumerate(degrees):
        vander = np.vander(x, degree)
        fit = np.poly1d(la.lstsq(vander, y)[0])
        
        axs[i].scatter(x, y, color='red', marker='x',label='Data')
        axs[i].plot(x_smooth, fit(x_smooth), label=f' Degree {degree} Curve Fit')
        axs[i].spines['top'].set_visible(False)
        axs[i].spines['right'].set_visible(False)
        axs[i].legend()   
    fig.suptitle("Purchase-Only Housing Price Index by Year")
    fig.supxlabel("Years since 2000")
    fig.supylabel("Price Index")
    plt.show()



def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """

    ellipse_data = np.load("LeastSquares_Eigenvalues/ellipse.npy")
    x, y = ellipse_data[:, 0], ellipse_data[:, 1]
    degree = 5
    vander = np.vander(x, degree)
    fit = la.lstsq(vander, y)[0]
    plot_ellipse(1, 1, 2, 1, 1)
    plt.show()


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")

ellipse_fit()