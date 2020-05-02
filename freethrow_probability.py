'''What's the probability of someone making a certain amount of free throws 
in a row given their free throw success percentage? 
If Sally makes 50% of her free shot throws, 
then Sally's probability of making 5 in a row would be 3%.'''

def free_throws(success, rows):
    success = int(success.strip('%')) *.01
    result = success
    while rows >1:
        result *= success
        rows -= 1
        
    result = round(result *100)
    
    return str(result)+'%'
    
print(free_throws('90%', 30))