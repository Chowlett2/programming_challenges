'''Create a function that takes a string and censors words over 
four characters with *.'''

def censor(s):
    lst = s.split(' ')
    for n, i in enumerate(lst):
        if len(i) > 4:
            lst[n] = '*'*len(i)
    return ' '.join(lst)