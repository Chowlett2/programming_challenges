'''In music, cadences act as punctuation in musical phrases, and help to mark 
the end of phrases. Cadences are the two chords at the end of a phrase. 

The different cadences are as follows:

V followed by I is a Perfect Cadence
IV followed by I is a Plagal Cadence
V followed by Any chord other than I is an Interrupted Cadence
Any chord followed by V is an Imperfect Cadence

Create a function where given a chord progression as a list, 
return the type of cadence the phrase ends on.'''

def find_cadence(chords):
    if chords[-2] == 'V':
        if chords[-1] == 'I':
            return 'perfect'
        return 'interrupted'
    if chords[-2] == 'IV' and chords[-1] == 'I':
        return 'plagal'
    if chords[-1] == 'V':
        return 'imperfect'
    return 'no cadence'