from Genevas import*
id1 = Genevas()
"""
from Andlat import*
id2 = Andlat()
"""

#This checks the name of the ID the player selected, and returns it
def checkId(names, id):
	playerSelects = names[id]
	return "You have selected " + playerSelects
	
#This later would be in a part of the code that refers to the individual player, checking which hero he/she selects
def playerCheck():
	names = ["Genevas", "Andlat", "Christina", "Tor", "Ophelia", "Silias", "Merrie", "Vorspiel", "Lace", "Galath", "Chips", "Tana", "Grace", "Vant", "Kyl", "Naru", "Alex"]
	id = int(input("Enter in your hero: "))-1
	print(checkId(names, id))
	playerCheck()

#This is where stats of the player can be called
def callStats():
	playerStats = id1.retrieveStats()

	
#Here is where the Game Starts
print("Welcome to the Gythian Civil War Battle Simulator.")
print("Please input the number of players.")
players = int(input())

playerCheck()
