'''A city skyline can be represented as a 2-D list with 1s representing buildings.
Create a function that takes a skyline (2-D list of 0's and 1's)
and returns the height of the tallest skyscraper.'''

def tallest_skyscraper(lst): 
    lstLen = len(lst)
    col1 = col2 = col3 = col4 = 0
    index1 = 0
    index2 = 0
    while index2 < 4:
        while index1 < lstLen:
            col1 += lst[index1][index2]
            index1 += 1
        index2 += 1
        index1 = 0
        while index1 < lstLen:
            col2 += lst[index1][index2]
            index1 += 1
        index2 += 1
        index1 = 0
        while index1 < lstLen:
            col3 += lst[index1][index2]
            index1 += 1
        index2 += 1
        index1 = 0
        while index1 < lstLen:
            col4 += lst[index1][index2]
            index1 += 1
        index2 += 1
    return max(col1, col2, col3, col4)