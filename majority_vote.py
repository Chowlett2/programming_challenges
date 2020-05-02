'''Create a function that returns the majority vote in a list. 
A majority vote is an element that occurs > N/2 times in a list 
(where N is the length of the list).'''

def majority_vote(lst):
    final = {}
    for i in set(lst):
        final.update({i : 0})
    for i in lst:
        final[i] += 1
    for i in final:
        if final[i]/ len(lst)>0.5:
            return i
