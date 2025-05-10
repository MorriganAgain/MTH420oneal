# qr_decomposition.py
"""Volume 1: The QR Decomposition.
<Finian O'Neal>
<MTH 420>
<5/9/25>
"""

import numpy as np
from scipy import linalg as la


# Problem 1
def qr_gram_schmidt(A):
    """Compute the reduced QR decomposition of A via Modified Gram-Schmidt.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n.

    Returns:
        Q ((m,n) ndarray): An orthonormal matrix.
        R ((n,n) ndarray): An upper triangular matrix.
    """
    
    m, n = np.shape(A)
    Q = np.copy(A)
    R = np.zeros((n, n))
    
    for i in range(0, n):
        R[i, i] = la.norm(Q[:, i])
        Q[:, i] = Q[:, i] / R[i, i]
        
        for j in range(i+1, n):
            R[i, j] = Q[:, j].T @ Q[:, i]
            Q[:, j] = Q[:, j] - R[i, j] * Q[:, i]
    
    return Q, R


# Problem 2
def abs_det(A):
    """Use the QR decomposition to efficiently compute the absolute value of
    the determinant of A.

    Parameters:
        A ((n,n) ndarray): A square matrix.

    Returns:
        (float) the absolute value of the determinant of A.
    """
    return np.prod(np.diag(qr_gram_schmidt(A)[1]))


# Problem 3
def solve(A, b):
    """Use the QR decomposition to efficiently solve the system Ax = b.

    Parameters:
        A ((n,n) ndarray): An invertible matrix.
        b ((n, ) ndarray): A vector of length n.

    Returns:
        x ((n, ) ndarray): The solution to the system Ax = b.
    """
    m, n = np.shape(A)
    Q, R = qr_gram_schmidt(A)
    y = Q.T @ b
    x = np.zeros(np.shape(b))
    x[n-1] = y[n-1] / R[n-1, n-1]
    for i in range(n, 0, -1 ):
        x[i-1] = (y[i-1] - np.sum(R[i-1,i:] @ x[i:])) / R[i-1, i-1]
        
    return x
    


# Problem 4
def qr_householder(A):
    """Compute the full QR decomposition of A via Householder reflections.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n.

    Returns:
        Q ((m,m) ndarray): An orthonormal matrix.
        R ((m,n) ndarray): An upper triangular matrix.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def hessenberg(A):
    """Compute the Hessenberg form H of A, along with the orthonormal matrix Q
    such that A = QHQ^T.

    Parameters:
        A ((n,n) ndarray): An invertible matrix.

    Returns:
        H ((n,n) ndarray): The upper Hessenberg form of A.
        Q ((n,n) ndarray): An orthonormal matrix.
    """
    raise NotImplementedError("Problem 5 Incomplete")

