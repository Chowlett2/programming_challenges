'''Create a function that concatenates n input lists, where n is variable.'''

def concat(*args):
    final = []
    for i in args:
        for j in i:
            final.append(j)
    return final
print(concat([1, 2, 3], [4, 5], [6, 7]))