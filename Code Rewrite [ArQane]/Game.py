from Genevas import*
id1 = Genevas()
"""
from Andlat import*
id2 = Andlat()
"""
	
#This checks the name of the ID the player selected, and returns it
def checkId(names, id):
	playerSelects = names[id]
	return playerSelects
	
#This later would be in a part of the code that refers to the individual player, checking which hero he/she selects
def playerCheck():
	names = ["Genevas", "Andlat", "Christina", "Tor", "Ophelia", "Silias", "Merrie", "Vorspiel", "Lace", "Galath", "Chips", "Tana", "Grace", "Vant", "Kyl", "Naru", "Alex"]
	id = int(input("\nEnter in your hero: "))-1
	playerHeroID.append(id)
	print("You have selected " + checkId(names, id))
	return checkId(names, id)
	
#Checks the stats and IDs for the player the user calls for
def statCheck():
	i = int(input("\nChoose the player you wish to check: "))-1
	print("\n" + players[i] + "'s hero is: " + playerHeroes[i])
	print("The ID of " + playerHeroes[i] + " is " + str(playerHeroID[i]))

#This is where stats of the player can be called
def callStats():
	playerStats = id1.retrieveStats()

	
#Here is where the Game Starts
print("Welcome to the Gythian Civil War Battle Simulator.")
print("Please input the number of players.")
playerNum = int(input())
#The player ID, or each individual player
players = []
#The name of the hero each player selected
playerHeroes = []
#The ID of the hero each player selected
playerHeroID = []

#Creates playerIDs
for x in range(1, playerNum+1):
	a = "Player " + str(x)
	players.append(a)
	
for i in players:
	playerHeroes.append(playerCheck())

statCheck()
