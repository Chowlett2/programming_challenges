'''Return the total number of lists inside a given list.'''

def num_of_sublists(lst):
    final = []
    for i in lst:
        if type(i) is list:
            final.append(i)
    return len(final)