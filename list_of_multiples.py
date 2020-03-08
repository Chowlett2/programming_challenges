'''Create a function that takes two numbers as arguments (num, length) and 
returns a list of multiples of num up to length.'''

def list_of_multiples(x, y):
    
    result = []
    index = 0
    z = x
    
    while index < y:
        result.append(z)
        z += x
        index += 1
    return result