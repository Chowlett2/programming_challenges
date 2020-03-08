'''Welcome to part two of the collection for Computer Science Algorithms. 
This challenge will deal further with writing recursive functions by covering 
the Euclidean Algorithm. The "Euclidean Algorithm" is a method for finding the 
greatest common divisor (GCD) of two numbers. It was originally described by 
the Greek mathematician Euclid.

Algorithm:
For the sake of simplicity I'll refer to the first number as "a", the second 
number as "b", and the remainder as "r". The algorithm can be broken down 
into four steps:

Ensure that "a" >= "b". If "a" < "b", swap them.
Find the remainder. Divide "a" by "b" and set "r" as the remainder.
Is "r" zero? If so terminate the function and return "b" (the second number).
Set "a" = "b" and "b" = "r" and start the algorithm over again.
Instructions
Create a recursive function that returns the GCD between two positive
numbers using the Euclidean Algorithm.'''

def euclidean(a, b):
    if b > a:
        return euclidean(b, a)
    r = a%b
    if r == 0:
        return b
    a = b
    b = r
    return euclidean(a, b)