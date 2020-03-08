'''Create a function that takes an amount of monetary change (e.g. 47 cents) 
and breaks down the most efficient way that change can be made using USD 
quarters, dimes, nickels and pennies. Your function should return a dictionary.'''

def make_change(c):
    result = {'q':0, 'd':0, 'n':0, 'p':0}
    while c > 0:
        if c - 25 >= 0:
            result['q'] += 1
            c -= 25
            continue
        if c - 10 >= 0:
            result['d'] += 1
            c -= 10
            continue
        if c - 5 >= 0:
            result['n'] += 1
            c -= 5
            continue
        if c - 1 >= 0:
            result['p'] += 1
            c -= 1
            continue
    return result