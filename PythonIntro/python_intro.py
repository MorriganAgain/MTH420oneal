# python_intro.py
"""Python Essentials: Introduction to Python.
<Finian O'Neal>
<MTH 420>
<4/16/25>
"""


# Problem 1 (write code below)
# Moved to bottom for testing :) 

# Problem 2
def sphere_volume(r):
    """ 
    Returns the volume a sphere of radius 'r'.
    """
    pi = 3.14159 
    return (4/3) * pi * r**3


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a, b, sep="     ", end="     ")
    print(c, d ,e)


# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    str_len = len(my_string)
    return my_string[0:int(str_len / 2)]
    
    

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    strange_animal_list = ["bear", "ant", "cat", "dog"]
    strange_animal_list.append("eagle")
    strange_animal_list[2] = "fox"
    strange_animal_list.pop(1)
    strange_animal_list.sort(reverse=True)
    strange_animal_list[strange_animal_list.index("eagle")] = "hawk"
    strange_animal_list[-1] = strange_animal_list[-1] + "hunter"
    
    
    return strange_animal_list


# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.
        if word starts w/ vowel -> add "hay" to end
        else move first char to end + "ay"
    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    vowels = ["a", "i", "e", "o", "u"]
    if word[0] in vowels:
        return word + "hay"
    return word[1:] + word[0] + "ay"


# Problem 7

def check_palindromity(num):
    if str(num)[0:3] == str(num)[::-1][0:3]: 
        return True
    return False

def palindrome():
    """ Find and retun the largest palindromic number made from the product
    of two 3-digit numbers.
    (# that reads same way, EX 1001, 696)
    """
    # generate nums -> check if palindromic -> check if highest 
    largest_palindrome = 0
    for i in range(500, 999):
        for j in range(500, 999):
            num = i * j
            if check_palindromity(num) == True and num > largest_palindrome:
                largest_palindrome = num
    return largest_palindrome

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    
    n_list = [((-1)**(i+1)/i) for i in range(1,n+1)]
    alt_harmonic = sum(n_list)
    return alt_harmonic

if __name__ == "__main__":
    print("Hello World!")
    print(sphere_volume(1))  # should return 4/3 * pi = 4.189
    isolate(1, 2, 3, 4, 5)
    print(first_half("half"))
    print(backward("half"))
    print(list_ops())
    print(pig_latin("apple"))
    print(pig_latin("banana"))
    print(palindrome())
    print(alt_harmonic(10))
