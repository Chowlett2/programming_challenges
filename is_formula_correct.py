'''Create a function that takes a string and returns True or False depending on whether or not the given formula is correct.

Examples:
formula("6 * 4 = 24") ➞ True

formula("18 / 17 = 2") ➞ False

formula("") ➞ None''''

def formula(txt):
    if txt =='':
        return None
    txt = txt.replace('a', '4')
    expressions = txt.split('=')
    totals = []
    for i in expressions:
        totals.append(float(eval(i)))
    return len(set(totals)) == 1