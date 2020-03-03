'''Create a function that takes a list of # and -, where each hash (#)
represents a mine and each dash (-) represents a mine-free spot. 
Return a list where each dash is replaced by a digit indicating the number 
of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).'''

def num_grid(lst):
    for i in lst:
        for n, j in enumerate(i):
            if j == '-':
                i[n] = 0
    for l, i in enumerate(lst):
        for n, j in enumerate(i):
            if j == '#':
                try:
                    if n != 0:
                        lst[l][n-1] += 1
                except:
                    IndexError    
                try:
                    lst[l][n+1] += 1
                except:
                    IndexError
                if l != 0:
                    try:
                        if n != 0:
                            lst[(l-1)][n-1] += 1
                    except:
                        IndexError
                    try:
                        lst[(l-1)][n] += 1
                    except:
                        IndexError
                    try:
                        lst[(l-1)][n+1] += 1
                    except:
                        IndexError
                if l != 4:
                    try:
                        if n != 0:
                            lst[(l+1)][n-1] += 1
                    except:
                        IndexError
                    try:
                        lst[(l+1)][n] += 1
                    except:
                        IndexError
                    try:
                        lst[(l+1)][n+1] += 1
                    except:
                        IndexError
    for i in lst:
        for n, j in enumerate(i):
            i[n] = str(i[n])
    return lst