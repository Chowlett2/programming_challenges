'''Create a function that takes in a list of intervals and returns how many 
intervals overlap with a given point.
An interval overlaps a particular point if the point exists inside the 
interval, or on the interval's boundary. For example the point 3 overlaps with 
the interval [2, 4] (it is inside) and [2, 3] (it is on the boundary).'''

def count_overlapping(intervals, point):
    total=0
    for i in intervals:
        if i[-1] >= point and i[0] <= point:
            total += 1
    return total