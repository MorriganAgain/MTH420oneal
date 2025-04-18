# standard_library.py
"""Python Essentials: The Standard Library.
<Finian O'Neal>
<MTH 420>
<4/18/25>
"""

from math import sqrt
from itertools import combinations


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L)/len(L)


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    mutability = {}
    # ints 
    int_1 = int(1)
    int_2 = int_1
    int_2 += 1
    if int_1 == int_2:
        mutability["integers"] = True
    else:
        mutability["integers"] = False
    # strings
    str_1 = "test"
    str_2 = str_1
    str_2 = "bop"
    if str_1 == str_2:
        mutability["strings"] = True
    else: mutability["strings"] = False
    # lists
    list_1 = [1, 2, 3]
    list_2 = list_1
    list_2[0] = 4
    print(list_1, list_2)
    if list_1 == list_2:
        mutability["lists"] = True
    else:
        mutability["lists"] = False
    # tuples
    tuple_1 = (1, 0)
    tuple_2 = tuple_1
    tuple_2 += (1, 0)
    if tuple_1 == tuple_2:
        mutability["tuples"] = True
    else:
        mutability["tuples"] = False
    # sets
    set_1 = {"a", "b"}
    set_2 = set_1
    set_2.add("c")
    if set_1 == set_2:
        mutability["sets"] = True
    else:
        mutability["sets"] = False
    
    return mutability


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return sqrt(a**2 + b**2)


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    power_set = []
    for i in range(len(A)+1):
        power_set.append(list(combinations(A, i)))

    return power_set

# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")

if __name__ == "__main__":
    print(prob1([1,2,3]))
    print(prob2())
    print(power_set("ABC"))
    
