'''John is playing a dice game. The rules are as follows.

Roll two dice.
Add the numbers on the dice together.
Add the total to your overall score.
Repeat this for three rounds.
But if you roll DOUBLES, your score is instantly wiped to 0 and 
your game ends immediately!

Create a function that takes in a list of tuples as input, and return 
John's score after his game has ended.'''

def diceGame(lst):
    total = 0
    for i in lst:
        if i[0] == i[1]:
            return 0
        else:
            total += i[0] + i[1]
    return total