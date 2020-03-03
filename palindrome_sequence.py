'''Make a function that takes a palindrome as it's an argument and returns 
the smallest seed integer that will produce that palindrome, 
along with the number of steps required'''

def pal_seq(n):
    seed=1
    steps=0
    
    while True:
        i=seed
        while i<n and str(i)!=str(i)[::-1]:
			i+=int(str(i)[::-1])
			steps+=1
		if i==n:
			return (seed,steps)
		seed+=1
		steps=0