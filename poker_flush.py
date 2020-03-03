'''Create a function that takes in two lists and determines whether there exists a flush.
The first list represents the 5 cards dealt on the table.
The second list represents the 2 cards in your hand.'''

def check_flush(table, hand):
    total = table + hand
    d, s, h, c = 0, 0, 0, 0
    for i in total:
        if "H" in i:
            h += 1
        if "D" in i:
            d += 1
        if "S" in i:
            s += 1
        if "C" in i:
            c += 1
    if h >= 5:
        return True
    if d >= 5:
        return True
    if s >= 5:
        return True
    if c >= 5:
        return True
    return False