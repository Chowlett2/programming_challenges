'''Write a function that inserts a white space between every instance of a 
lower character followed immediately by an upper character.'''

def insert_whitespace(txt):
	return ''.join([' '+x if x == x.upper() else x for x in txt])[1:]