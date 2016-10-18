from Genevas import*
id1 = Genevas()
"""
from Andlat import*
id2 = Andlat()
from Christina import*
id3 = Christina()
from Tor import*
id4 = Tor()
from Ophelia import*
id5 = Ophelia()
from Silias import*
id6 = Silias()
from Merrie import*
id7 = Merrie()
from Vorpspiel import*
id8 = Vorspiel()
from Lace import*
id9 = Lace()
from Galath import*
id10 = Galath()
from Chips import*
id11 = Chips()
from Tana import*
id12 = Tana()
from Grace import*
id13 = Grace()
from Vant import*
id14 = Vant()
from Kyl import*
id15 = Kyl()
from Naru import*
id16 = Naru()
from Alex import*
id17 = Alex()
"""
	
#This checks the name of the ID the player selected, and returns it
def checkId(names, id):
	playerSelects = names[id]
	return playerSelects
	
#This later would be in a part of the code that refers to the individual player, checking which hero he/she selects
def playerCheck(n):
	names = ["Genevas", "Andlat", "Christina", "Tor", "Ophelia", "Silias", "Merrie", "Vorspiel", "Lace", "Galath", "Chips", "Tana", "Grace", "Vant", "Kyl", "Naru", "Alex"]
	id = int(input("\nEnter in your hero: "))-1
	playerHeroID.append(id)
	print(str(players[n]) + " has selected " + checkId(names, id))
	return checkId(names, id)
	
#Checks the stats and IDs for the player the user calls for
def statCheck():
	i = int(input("\nChoose the player you wish to check: "))-1
	print("\n" + players[i] + "'s hero is: " + playerHeroes[i])
	print("The ID of " + playerHeroes[i] + " is " + str(playerHeroID[i]))
	print("Health: " + str((callStats(playerHeroID[i])[0])))
	print("Stamina: " + str((callStats(playerHeroID[i])[1])))
	print("Mana: " + str((callStats(playerHeroID[i])[2])))
	print("Ammo: " + str((callStats(playerHeroID[i])[3])))
	print("Physical Attack: " + str((callStats(playerHeroID[i])[4])))
	print("Magical Attack: " + str((callStats(playerHeroID[i])[5])))
	print("Technological Attack: " + str((callStats(playerHeroID[i])[6])))
	print("Physical Defense: " + str((callStats(playerHeroID[i])[7])))
	print("Magical Defense: " + str((callStats(playerHeroID[i])[8])))
	print("Technological Defense: " + str((callStats(playerHeroID[i])[9])))

#This is where stats of the player can be called
def callStats(n):
	playerStats = []
	idcheck = eval("id" + str(n + 1))
	playerStats = idcheck.retrieveStats()
	return playerStats

	
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
	
for i in range(0, len(players)):
	playerHeroes.append(playerCheck(i))

statCheck()
