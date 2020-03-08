'''Create a function that returns all combinations of size n from a list. 
Sort the list in ascending lexicographical order.'''

from itertools import combinations
def combo(lst, n):
    result = []
    test = list(combinations(lst, n))
    for i in test:
        result.append(list(i))
    return result