'''A ship has to transport cargo from one place to another, 
while picking up cargo along the way. Given the total amount of cargo 
and the types of cargo holds in the ship as lists, create a function that returns True 
if each weight of cargo can fit in one hold, and False if it can't.

"S" means 50 cargo space.
"M" means 100 cargo space.
"L" means 200 cargo space.'''

def will_fit(holds, cargo):
    total = len(holds)
    index = 0
    while index < total:
        if holds[index] == 'S':
            if cargo[index] > 50:
                return False
        elif holds[index] == 'M':
            if cargo[index] > 100:
                return False
        else:
            if cargo[index] > 200:
                return False
        index += 1
    return True