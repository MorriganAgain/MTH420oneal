# drazin.py
"""Volume 1: The Drazin Inverse.
<Finian O'Neal>
<MTH 420>
<5/15/25>
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    
    cond_1 = np.allclose(A @ Ad, Ad @ A)
    cond_2 = np.allclose(np.linalg.matrix_power(A, k+1) @ Ad, np.linalg.matrix_power(A, k))
    cond_3 = np.allclose(Ad @ A @ Ad, Ad)
    
    if cond_1 and cond_2 and cond_3:
        return True
    return False


# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    
    n, n = np.shape(A)
    Z = np.zeros((n, n))
    f_1 = lambda x: abs(x) > 0
    f_2 = lambda x: abs(x) <= 0
    T_1, Q_1, k_1 = la.schur(A, sort=f_1)
    T_2, Q_2, k_2 = la.schur(A, sort=f_2)
    U = np.concatenate([Q_1[:, :k_1], Q_2[:, :n-k_1]], 1)
    U_inv = la.inv(U)
    V = U_inv @ A @ U
    
    if np.isclose(k_1, 0, tol) == False:
        M_inv = la.inv(V[:k_1, :k_1])
        Z[:k_1, :k_1] = M_inv 
    
    return U @ Z @ U_inv

def laplacian(A):
    """Compute the Laplacian matrix of the adjacency matrix A,
    as well as the second smallest eigenvalue.

    Parameters:
        A ((n,n) ndarray) adjacency matrix for an undirected weighted graph.

    Returns:
        L ((n,n) ndarray): the Laplacian matrix of A
    """
    D = A.sum(axis=1)    # The degree of each vertex (either axis).
    return np.diag(D) - A


# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    
    n, n = np.shape(A)
    L = laplacian(A)
    I = np.identity(n)
    R = np.zeros((n, n))
    
    for row in range(0, n):
        L_tilda = np.copy(L)
        L_tilda[row, :] = I[row, :]
        R_val = drazin_inverse(L_tilda)
        
        for col in range(0, n):
            if row == col:
                R[row, col] = 0
            else:
                R[row, col] = R_val[col, col]
    return R


# Problems 4 and 5
class LinkPredictor:
    """Predict links between nodes of a network."""

    def __init__(self, filename='social_network.csv'):
        """Create the effective resistance matrix by constructing
        an adjacency matrix.

        Parameters:
            filename (str): The name of a file containing graph data.
        """
        raise NotImplementedError("Problem 4 Incomplete")


    def predict_link(self, node=None):
        """Predict the next link, either for the whole graph or for a
        particular node.

        Parameters:
            node (str): The name of a node in the network.

        Returns:
            node1, node2 (str): The names of the next nodes to be linked.
                Returned if node is None.
            node1 (str): The name of the next node to be linked to 'node'.
                Returned if node is not None.

        Raises:
            ValueError: If node is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")


    def add_link(self, node1, node2):
        """Add a link to the graph between node 1 and node 2 by updating the
        adjacency matrix and the effective resistance matrix.

        Parameters:
            node1 (str): The name of a node in the network.
            node2 (str): The name of a node in the network.

        Raises:
            ValueError: If either node1 or node2 is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")

"""A = np.array([[1, 3, 0, 0],
              [0, 1, 3, 0],
              [0, 0, 1, 3],
              [0, 0, 0, 0]])
Ad = np.array([[1, -3, 9, 81],
              [0, 1, -3, -18],
              [0, 0, 1, 3],
              [0, 0, 0, 0]])
k=1

test = np.array([[0, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0]])
test2 = np.array([[0, 1, 1], 
                  [1, 0, 1],
                  [1, 1, 0]])

print(effective_resistance(test2))"""

A = np.array([[ 10,  -8,   6,  -3,],
                [ 12, -10,   8,  -4,],
                [  1,  -1,   1,   0,],
                [ -2,   2,  -2,   2]])
print(drazin_inverse(A))

