'''Create a function that takes a string txt and censors any word from a given list lst. 
The text removed must be replaced by the given character char.'''

def censor_string(txt, lst, character):
    for word in lst:
        txt = txt.replace(word, character*len(word))
    return txt