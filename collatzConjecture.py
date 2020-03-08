'''A Collatz sequence is generated like this. Start with a positive number. 
If it's even, halve it. If it's odd, multiply it by 3 and add one. Repeat the 
process with the resulting number. The Collatz Conjecture is that every 
sequence eventually reaches 1 (continuing past 1 just results in an endless 
repeat of the sequence (4, 2, 1)).

The length of the sequence from starting number to 1 varies widely.

Create a function that takes a number as an argument and returns a tuple of 
two elements — the number of steps in the Collatz sequence of the number, 
and the highest number reached.'''

def collatz(n):
    lst = []
    while True:
        if n == 1:
            lst.append(int(n))
            return (len(lst), max(lst))
        elif n % 2 == 0:
            lst.append(int(n))
            n = n/2
        else:
            lst.append(int(n))
            n = (n * 3) + 1