'''Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"'''

def encrypt(string):
    
    result = ''
    backwards = ''
    index = len(string)
    count = -1
    
    while abs(count) <= index:
        backwards += string[count]
        count -= 1
            
    for i in backwards:
        if i == 'a':
            i = '0'
        if i == 'e':
            i = '1'
        if i == 'o':
            i = '2'
        if i == 'u':
            i = '3'
        result += i
    
    result += 'aca'
    
    return result