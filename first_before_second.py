'''You are given three inputs: a string, one letter, and a second letter.
Write a function that returns True if every instance of the first letter 
occurs before every instance of the second letter.'''

def first_before_second(s, first, second):
    lst = []
    for i in s:
        if i is first or i is second:
            lst.append(i)
    sort = sorted(lst)
    rev = sort[::-1]
    if lst[0] is first:
        return sort == lst or rev == lst
    return False