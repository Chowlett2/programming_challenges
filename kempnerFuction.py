'''The Kempner Function, applied to a composite number, permits to find the 
smallest integer greater than zero which factorial is exactly divided by 
the number.'''

def kempner(n):
    fact = 1
    for i in range(1, n+1):
        if fact*i%n == 0:
            return i
        else:
            fact = fact*i