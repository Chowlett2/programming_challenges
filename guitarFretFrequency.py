'''Create a function that takes a number of a guitar string and the number of 
the fret and returns the corresponding frequency of the note.

Check the Resources Tab, for the correct frequencies per string.
The formula to calculate the frequency is: String Frequency * 2**(fret/12).
Round the frequency to the nearest hundreth.
For this challenge, we use "Standard Tuning".'''

def fret_freq(g_str, fret):
    if g_str == 1:
        return round(329.63 * 2 ** (fret/12), 2)
    if g_str == 2:
        return round(246.94 * 2 ** (fret/12), 2)
    if g_str == 3:
        return round(196.00 * 2 ** (fret/12), 2)
    if g_str == 4:
        return round(146.83 * 2 ** (fret/12), 2)
    if g_str == 5:
        return round(110.00 * 2 ** (fret/12), 2)
    if g_str == 6:
        return round(82.41 * 2 ** (fret/12), 2)