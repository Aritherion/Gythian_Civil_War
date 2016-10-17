import random

#list of battle IDs:
# 1:Genevas  2:Andy  3:Tina  4:Tor  5:Ophelia  6:Silas  7:Merrie  8:Vorspiel  9:Lace  10:Galath  11:Vihjalmur  12:Chips  13:Tana  14:Stockholm  15:Grace  16:Vant  17:Kyl  18:Naru  19:Alex
# 11:Vihjalmur and 14:Stockholm are no longer relavant
#17: Kyl has no stats or attacks
#8: Vorspiel and 18: Naru has no attacks
#How stats are listed:
#stats: HP, SP, FP, AP, PA, MA, TA, PD, MD, TD
#effects such as buffs and debuffs are added on to the end of the list during the battle

#This nametoid function takes in a string 'name' and puts out an int 'id'
#If there is no hero by the name, it will output 0.
def nametoid(name):
	if(name == "Genevas"):
		id = 1
	elif(name == "Andlat"):
		id = 2
	elif(name == "Christina"):
		id = 3
	elif(name == "Tor"):
		id = 4
	elif(name == "Ophelia"):
		id = 5
	elif(name == "Silas"):
		id = 6
	elif(name == "Merrie"):
		id = 7
	elif(name == "Vorspiel"):
		id = 8
	elif(name == "Lace"):
		id = 9
	elif(name == "Galath"):
		id = 10
	elif(name == "Chips"):
		id = 12
	elif(name == "Tana"):
		id = 13
	elif(name == "Grace"):
		id = 15
	elif(name == "Vant"):
		id = 16
	elif(name == "Kyl"):
		id = 17
	elif(name == "Naru"):
		id = 18
	elif(name == "Alex"):
		id = 19
	else:
		id = 0
	return id

#this idtoname function takes in an int 'id' and puts out a string 'name'
def idtoname(id):
	if(id == 1):
		name = "Genevas"
	elif(id == 2):
		name = "Andlat"
	elif(id == 3):
		name = "Christina"
	elif(id == 4):
		name = "Tor"
	elif(id == 5):
		name = "Ophelia"
	elif(id == 6):
		name = "Silias"
	elif(id == 7):
		name = "Merrie"
	elif(id == 8):
		name = "Vorspiel"
	elif(id == 9):
		name = "Lace"
	elif(id == 10):
		name = "Galath"
	elif(id == 12):
		name = "Chips"
	elif(id == 13):
		name = "Tana"
	elif(id == 15):
		name = "Grace"
	elif(id == 16):
		name = "Vant"
	elif(id == 17):
		name = "Kyl"
	elif(id == 18):
		name = "Naru"
	elif(id == 19):
		name = "Alex"
	return(name)

#this attacks function takes in id, attack, and order
#id is the Battle ID of the Attacker
#attack is the attack number of the attack
#order is the order of the attacker on the orderlist. 
#This helps locate the attackers stats from the statslist.
#The function outputs a boolean veriable
#If the attacker makes a move, it returns True.
#If the attacker fails to make a move, it returns False.
def attacks(id, attack, order):
	global orderlist
	global statslist
	attackerstats = statslist[order]
	if (id == 1):
		#Come Hither, Technological Attack, Physical Damage.
		#10 SP
		#Genevas either grapples to somebody or grapples them to him. If the target's HP is less than Genevas's, do the latter, if not, former.
		#If the former, it deals 15 damage and prevents an escape attempt
		#If the latter, it deals 20 damage and reduces their PD and TD by 1
		if (attack == 1):
			#if Genevas does not have enough Stamina, this attack will cancel, and the function will return False.
			if (attackerstats[1] < 10):
				print("You do not have enough Stamina to do this.")
				return False
			else:
				print("Please input the battle ID of your target.")
				targetvalid = False
				#This loop will keep running until a valid target is input.
				while (targetvalid == False):
					target = input()
					try:
						orderlist.index(target)
					except ValueError:
						print("Your target is not in the fight. Please try again.")
						continue
					targetvalid = True
				#You have your battle ID of your target stored in the variable 'target' at this point.
				targetorder = orderlist.index(target)
				targetstats = statslist[targetorder]
				#Now, you have both the attacker's stats and the target's stats.
				temp = attackerstats[1]
				temp = temp - 10
				attackerstats[1] = temp
				attackersroll = random.randrange(1, 21)
				print("Genevas rolled " + str(attackersroll) + " from a D20.")
				defendersroll = random.randrange(1, 21)
				print(idtoname(target) + " rolled " + str(defendersroll) + " from a D20.")
				finalattackvalue = attackerstats[6] + attackersroll
				print("Genevas's final attack value is " + str(finalattackvalue))
				finaldefensevalue = targetstats[7] + defendersroll
				print(idtoname(target) + "'s final defense value is " + str(finaldefensevalue))
				#This conditional is when the attack hits.
				if (finalattackvalue > finaldefensevalue):
					print("Genevas's Come Hither hits " + idtoname(target) + "!")
					#If the target's HP is less than Genevas's, Genevas grapples the target to him.
					#Genevas deals 20 damage and reduces the target's PD and TD by 1.
					if (targetstats[0] < attackerstats[0]):
						print("Genevas grappled " + idtoname(target) + " to him!")
						temp = targetstats[0]
						targetstats[0] = (temp - 20)
						print("Genevas dealt 20 damage to " + idtoname(target) + "!")
						temp = targetstats[7]
						targetstats[7] = (temp - 1)
						temp = targetstats[9]
						targetstats[9] = (temp - 1)
						print("Genevas reduced " + idtoname(target) + "'s PD and TD by 1!")
					#If the target's HP is greater than or equal to Genevas's, Genevas grapples to the target.
					#Genvas deals 15 damage.
					else:
						temp = targetstats[0]
						targetstats[0] = (temp - 15)
						print("Genevas dealt 15 damage to " + idtoname(target) + "!")
				else:
					print("Genevas's Come Hither did not hit " + idtoname(target) + "!")
				statslist[order] = attackerstats
				statslist[targetorder] = targetstats
				return True

#This battleid fucntion is given the player's battle ID
#It outputs a list containing the Player's initial stats.
#Order of stats:
#HP, SP, FP, AP, PA, MA, TA, PD, MD, TD.
def battleid(a):
		if (a == 1):
			b = [350, 200, 0, 50, 25, 0, 25, 20, 15, 10]
		elif (a == 2):
			b = [220, 120, 500, 0, 24, 28, 0, 23, 18, 23]
		elif (a == 3):
			b = [50, 300, 300, 300, 4, 4, 4, 4, 4, 4]
		elif (a == 4):
			b = [300, 150, 200, 10, 15, 19, 1, 19, 19, 17]
		elif (a == 5):
			b = [300, 0, 0, 0, 20, 0, 30, 25, 25, 25]
		elif (a == 6):
			b =  [250, 100, 200, 0, 10, 20, 0, 15, 25, 10]
		elif (a == 7):
			b = [180, 30, 300, 0, 2, 30, 0, 20, 25, 20]
		elif (a == 8):
			b = [130, 160, 260, 150, 22, 22, 22, 15, 15, 15]
		elif (a == 9):
			b = [110,250,0,60,0,0,30,23,30,10]
		elif (a == 10):
			b = [250, 250, 0, 0, 35, 0, 0, 20, 15, 15]
		elif (a == 12):
			b = [150, 100, 210, 210, 10, 12, 21, 14, 14, 14]
		elif (a == 13):
			b = [0, 0, 300, 0, 0, 30, 0, 0, 25, 0]
		elif (a == 15):
			b = [26, 30, 300, 0, 2, 30, 0, 20, 25, 20]
		elif (a == 16):
			b = [400, 100, 200, 0, 20, 10, 0, 20, 20, 20]
#		elif (a == 17):
		elif (a == 18):
			b = [150, 200, 100, 0, 15, 15, 0, 15, 15, 20]
		elif (a == 19):
			b = [150, 300, 0, 0, 25, 0, 25, 10, 20, 20]
		return b

#This battle function is given the order of the player and the battle ID of the player
#It asks for the attack, and calls the attacks function
def battle(order, id):
	moved = False
	#This loop loops until the player makes a valid move.
	while (moved == False):
		if (id == 1):
			print("Your turn, Genvas Treeson.")
			print("Available Attacks: Come Hither(1), Chemical Blood(2), Toxin Trickery(3), Marauders Mutilation(4), Gender Fluid Trauma(5)")
			attack = input()
		elif (id == 2):
			print("your turn, Andlat Einarson Josdottir")
			print("(1)Metal Slash, (2) Shard Blast, (3) Root, (4) Iron Maiden, (5)Metal Toss, (6)Thunder, (7)Blood Leech, (8) Transfusion, (9) Shank, (10) Dance, (11) Shark Attack")
			attack = input()
		elif (id == 3):
			print("Your turn, Christina")
			print("Available attacks: MDF grenade(1), EMP grenade(2), Cripple(3), Flight(4), Cloaking(5), Medpack(6), Healing Artifact(7), Flashbang(8), Energy Transfer(9), Ammunition Station(10), Taze(11), Full On Attack(12), Hinder(13).")
			attack = input()
		elif (id == 4):
			print("Your turn, Tor Ranneth.")
			print("Available Attacks: I Like Big Buffs and I Cannot Lie (1), Rose Garden Filled With Thorns (3), Just like animals (4), Rivers in the Night (5), Freedom Feels Like Flying (6), Remember the Avocado (7), Various Nature themed attacks (8).")
			atttack = input()
		elif (id == 5):
			print("Your turn, X01148-F Ophelia")
			print("Available attacks: beep(1), boop(2), scanning(3), short circuit(4), recharge(5), terminate(6)")
			attack = input()
		elif (id == 6):
			print("Your turn, Silas Dent.")
			print("Available attacks: Shatterglass Song(1), Song of Repair(2), Brown Note(3), Lullaby(4), Fort-Etude(5), Dis-chord(6), Power Play(7), Allegro Vivace(8), Sad Violin(9), Wait for it...(10), The Silence(11), Cut Time(12)")
			attack = input()
		elif (id == 7):
			print("Your turn, Nachtmerrie Verslinder.")
			print("Available attacks: Daydreaming(1), Soul Wisp(2), Inner Demons(3), Goodnight!(4), Netherworld Portal(5), Snack Time(6)")
			attack = input()
		elif (id == 8):
			print("Your turn, Vorspiel.")
			print("Available attacks: N/A")
			attack = input()
		elif (id == 9):
			print("Your turn, Lace Wunderbar.")
			print("Available attacks: Stun Bomb(1), Damage Bomb(2), Smoke Bomb(3), Collateral Bomb(4), Poison Bomb(5), Incendiary Bomb(6), Bombgel Punch(7), Pedit Medpack(8)")
			attack = input()
		elif (id == 10):
			print("Your turn, Galath.")
			print("Available attacks: Armor Shred(1), Backstab(2), Counter(3), Deceptive Behavior(4), Playing Dirty(5), Speed or Power(6), Spine Breaker(7)")
			attack = input()
		elif (id == 12):
			print("Your turn, Gratha Tro'Urn")
			print("Available Attacks: Arm Canon (1), Dice Bomb (2), Blackflame (3), Seduction (4), MAGIC CARDS (5), Bitch Slap (6), Combo Shot (7), They Call Me Chips (8), Try Me (9), Thanks Morkin (10)")
			attack = input()
		elif (id ==13):
			print("Your turn, Tana.")
			print("Available attacks: Fire(1), Inferno(2), Fire V2.0(3), Fuel(4), Burn Out(5)")
			attack = input()
		elif (id == 15):
			print("Your turn, Grace Pandora.")
			print("Available attacks: Forced Evolution(1), Disease Cloud(2), Death's Remedy(3), Reconstruction Surgeon(4), Special Plague: Halcyon Sickness(5), Special Plague: Corrosion(6),  Glacier Shell(7), Cryo Blast(8), Frost Enchant(9), Frost Implosion(10), Vortex(11)")
			attack = input()
		elif (id == 16):
			print("Your turn, Vant Copil.")
			print("Available Attacks: Swing(1), Charging(2), Aiming Practice(3), It's Mine(4), Punching(5), I'll be There for you(6).")
			attack = input()
#		elif (id == 17):
		elif (id == 18):
			print("Your turn, Naru.")
			print("Available Attacks: N/A")
			attack = input()
		elif (id == 19):
			print("Your turn, Alexander Claus.")
			print("Downward Strike (1), Low Thrust (2), Backhand (3), Forward Knee (4), Hammer Down (5), Power Stab (6), Disabler (7), Scapula Fracture (8), Tibia Fissure (9).")
			attack = input()
		moved = attacks(id, attack, order)

#this function prints out the stats of a player from the input of his order in the order list
def printstats(order):
	global statslist
	print("Stats for player "+str(order+1))
	print statslist[order]

#def phaseeffects(order):

#def endphase(order):


	
	


print("Welcome to the Gythian Civil War Battle Simulator. Please input the number of players.")
players = int(input())

#The orderlist contains all the battle ID of the characters in the battle, in order of battle phase
orderlist = []
#The statslist contains all the stats list of all the characters in battle, in order of battle phase
statslist = []

#This loop completes the initial orderlist and statslist
for x in range(0, players):
	print("Please input your battle ID")
	a = int(input())
	#adds the battle ID to the order list
	orderlist.append(a)
	#adds the stats to the stats list
	statslist.append(battleid(a))
	
	
#i represents turns
i = 0
while True:
	i += 1
	#x represent phases.
	#There are as many phases as there are players, plus an extra end phase coded seperate of this for loop.
	for x in range(0, players):
		print("Turn " + str(i)+ " Phase " + str(x + 1))
		#This loop prints the stats of all players.
		for y in range(0, players):
			printstats(y)
		#This function should take care of all the moves in this phase.
		battle(x, orderlist[x])
		#this phaseeffects function should take care of all the effects such as DoTs.
		#phaseeffects(stats(order[x]))
	
	#this part codes for the end phase.
	print("Turn " + str(i)+ " End Phase")
	for y in range(0, players):
		#this loop prints the stats of all players in the end phase
		printstats(y)
	#for z in range(0, players):
		#this loop runs the end phase effects for all players
		#endphase(z)