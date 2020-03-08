'''A pandigital number contains all digits (0-9) at least once. 
Write a function that takes an integer, returning True if the integer is 
pandigital, and False otherwise.'''

def is_pandigital(n):
    unique = []
    for i in str(n):
        if i not in unique:
            unique.append(i)
    if len(unique) == 10:
        return True
    return False