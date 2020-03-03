'''Create a function that takes two timestamps as input, and returns a string describing the time 
elapsed between them (in days, hours, minutes, seconds as appropriate).'''

def elapsed(t1, t2):
    
    t3 = t2 - t1    
    second = 1
    minute = 60
    hour = 60 * minute
    day = 24 * hour    
    dayFinal = t3 // day
    t3 -= (day * dayFinal)
    hourFinal = t3 // hour
    t3 -= (hour * hourFinal)
    minuteFinal = t3 // minute
    t3 -= (minute * minuteFinal)
    secondFinal = t3
    final = ''
    
    while True:
        if dayFinal > 1:
            final += (str(dayFinal) + " days")
        elif dayFinal == 1:
            final += (str(dayFinal) + " day")
        if ((dayFinal >= 1) and (hourFinal > 0)) or ((dayFinal >= 1) and 
            (minuteFinal > 0)) or ((dayFinal >= 1) and (secondFinal > 0)):
            final += (", ")
            
        if hourFinal > 1:
            final += (str(hourFinal) + " hours")
        elif hourFinal == 1:
            final += (str(hourFinal) + " hour")
        if ((hourFinal >= 1) and 
            (minuteFinal > 0)) or ((hourFinal >= 1) and (secondFinal > 0)):
            final += (", ")            
        if minuteFinal > 1:
            final += (str(minuteFinal) + " minutes")
        elif minuteFinal == 1:
            final += (str(minuteFinal) + " minute")
        if ((minuteFinal >= 1) and (secondFinal > 0)):
            final += (", ")
            
        if secondFinal > 1:
            final += (str(secondFinal) + " seconds")
        elif secondFinal == 1:
            final += (str(secondFinal) + " second")
        break

    return final