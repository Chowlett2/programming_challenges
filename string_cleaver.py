'''Create a function that takes a string (without spaces) and a word list, 
cleaves the string into words based on the list, and returns the correctly spaced 
version of the string(a sentence). 
If a section of the string is encountered that can't be found on the word list, return
"Cleaving stalled: Word not found".'''

def cleave(string, lst):
    count = len(string)
    final = []
    loop = 0
    while string:
        if loop >1000:
            return 'Cleaving stalled: Word not found'
        if string [:count] in lst:
            final.append(string[:count])
            tempString = string
            string = string[count:]
            count=len(string)
        else:
            count-= 1
            if count == -1:
                final = final[:-1]
                final.append(tempString[count+1][0])
                string = tempString[1:]
        loop+=1
    return ' '.join(final)