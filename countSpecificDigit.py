'''Write a function that counts the number of times a specific digit occurs in 
a range (inclusive). 

The function will look like:

digit_occurrences(start, end, digit) ➞ number of times digit occurs'''

def digit_occurrences(start, end, digit):
    nums = ''
    for i in range(start, end + 1):
        nums += str(i)
    return nums.count(str(digit))