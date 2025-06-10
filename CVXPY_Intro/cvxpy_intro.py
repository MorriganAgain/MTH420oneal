# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Name>
<Class>
<Date>
"""

import numpy as np
import cvxpy as cp

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    
    x = cp.Variable(3, nonneg=True)
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c.T @ x)
    
    const_one = np.array([1, 2, 0])
    const_two = np.array([0, 1, -4])
    const_three = np.array([2, 10, 3])
    const_four = np.identity(3)
    
    constraint = [const_one @ x <= 3, const_two @ x <= 1, const_three @ x >= 12, const_four @ x >= 0]
    problem = cp.Problem(objective, constraint)
    solution = problem.solve()
    
    return x.value, solution



# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    
    x = cp.Variable(4, nonneg=True)
    l1 = cp.norm(x, 1)
    objective = cp.Minimize(l1)
    constraint = [A @ x == b]
    
    problem = cp.Problem(objective, constraint)
    solution = problem.solve()
    
    return x.value, solution


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    
    x = cp.Variable(6, nonneg=True)
    c = np.array([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize(c.T @ x)
    
    S = np.array([[1, 1, 0, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 1, 1]])
    
    S_max = np.array([7, 2, 4])
    
    D = np.array([[1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1]])
    
    D_val = np.array([5, 8])
    
    pos = np.identity(6)
    
    constraint = [S @ x <= S_max,D @ x == D_val, pos @ x >= 0]
    
    problem = cp.Problem(objective, constraint)
    solution = problem.solve()
    
    return x.value, solution


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    
    x = cp.Variable(3)
    Q = np.array([[3, 2, 1], 
                  [2, 4, 2],
                  [1, 2, 3]])
    r = np.array([3, 0, 1])
    
    problem = cp.Problem(cp.Minimize(0.5 * cp.quad_form(x, Q) + r.T @ x))
    solution = problem.solve()

    return x.value, solution


# Problem 5

def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    
    m, n = np.shape(A)
    x = cp.Variable(n, nonneg=True)
    objective = cp.Minimize(cp.norm(A @ x - b, 2))
    
    c1 = cp.sum(x)
    c2 = np.identity(n)
    
    constraint = [c1 == 1, c2 @ x >= 0]
    
    problem = cp.Problem(objective, constraint)
    solution = problem.solve()
    return x.value, solution


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")


A = np.array([[1, 2, 1, 1], 
              [0, 3, -2, -1]])
b = np.array([7, 4])
#print(prob5(A, b))
#print(prob4())
print(l1Min(A, b))