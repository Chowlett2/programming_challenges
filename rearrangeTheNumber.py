'''Given a number, return the difference between the maximum and minimum 
numbers that can be formed when the digits are rearranged.'''

def rearranged_difference(num):
    smallest = sorted(str(num))
    largest = reversed(smallest)
    return int(''.join(largest)) - int(''.join(smallest))