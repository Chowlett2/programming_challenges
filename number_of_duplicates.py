'''Create a function that returns the amount of duplicate characters in a string. 
It will be case sensitive and spaces are included. If there are no duplicates, 
return 0.'''

def duplicates(txt):
    return len(txt)-len(set(txt))