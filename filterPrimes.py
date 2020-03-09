'''Create a function that takes a list and returns a new list containing 
only prime numbers.'''

def filter_primes(num):
    nonPrime = []
    final = []
    for i in num:
        for x in range(2, i):
            if i%x == 0:
                nonPrime.append(i)
                break
    for i in num:
        if i not in nonPrime and i != 1:
            final.append(i)
    return final