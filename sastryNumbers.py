'''In this challenge, you have to establish if a given integer n is a Sastry number. 
If the number resulting from the concatenation of an integer n with its successor 
is a perfect square, then n is a Sastry Number.

Given a positive integer n, implement a function that returns True if n is a 
Sastry number, or False if it's not.'''

def is_sastry(n):
    return int(int(str(n)+str(n+1))**.5)==int(str(n)+str(n+1))**.5