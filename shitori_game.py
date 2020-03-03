'''This challenge is an English twist on the Japanese word game Shiritori.
The basic premise is to follow two rules:
1. First character of next word must match last character of previous word.
2. The word must not have already been said.

Write a Shiritori class that has two instance variables:

words: a list of words already said.
game_over: a boolean that is true if the game is over.
and two instance methods:

play: a method that takes in a word as an argument and checks if it is valid
(the word should follow rules #1 and #2 above).

If it is valid, it adds the word to the words list, and returns the words list.
If it is invalid (either rule is broken), it returns "game over" and sets the game_over boolean to true.
restart: a method that sets the words list to an empty one [] and sets the game_over boolean to false.
It should return "game restarted".'''

class Shiritori:
    
	def __init__(self):
		self.words = []
		self.game_over = False
	
	def play(self,new):
		if self.words==[] or (new[0]==self.words[-1][-1] and new not in self.words):
			self.words.append(new)
			return self.words
		self.game_over = True
		return "game over"
	
	def restart(self):
		self.__init__()
		return "game restarted"