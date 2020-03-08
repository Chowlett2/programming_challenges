'''Create a function that takes a number steps as an argument and returns 
the amount of rectangles you can count in a matrix.'''

def rectangles(step):
    result = 0
    while step > 0:
        result += step**3
        step -= 1
    return result