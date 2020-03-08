'''Create a function that takes an integer and outputs an n x n square solely 
consisting of the integer n.'''

def square_patch(n):
    if n == 0:
        return []
    x = []
    for i in range(n):
        x.append(n)
    y = []
    for i in range(n):
        y.append(x)
    return y