'''Given three numbers, x, y and z, determine whether they are the edges of 
a right angled triangle.'''

def right_triangle(x, y, z):
    ordered = [x, y, z]
    ordered.sort()
    if x <= 0 or y <= 0 or z <= 0:
        return False
    if ordered[0]**2 + ordered[1]**2 == ordered[2]**2:
        return True
    return False