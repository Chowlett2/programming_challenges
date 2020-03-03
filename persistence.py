'''The additive persistence of an integer, n, is the number of times you have to 
replace n with the sum of its digits until n becomes a single digit integer.

The multiplicative persistence of an integer, n, is the number of times you have to
replace n with the product of its digits until n becomes a single digit integer.

Create two functions that take an integer as an argument and:

Return its additive persistence.
Return its multiplicative persistence.'''

def additive_persistence(n):
    new = 0
    counter = 0
    while True:
        if n > 9:
            counter += 1
            for i in str(n):
                new += int(i)
        if new > 9:
            n = new
            new = 0
        else:
            break
    return counter
def multiplicative_persistence(n):
    new = 1
    counter = 0
    while True:
        if n > 9:
            counter += 1
            for i in str(n):
                new *= int(i)
        if new > 9:
            n = new
            new = 1
        else:
            break
    return counter