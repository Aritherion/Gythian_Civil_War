import random

#list of battle IDs:
# 1:Genevas  2:Andy  3:Tina  4:Tor  5:Ophelia  6:Silas  7:Merrie   
#8:Vorspiel  9:Lace  10:Galath  11:Vihjalmur  12:Chips  13:Tana   
#14:Stockholm  15:Grace  16:Vant  17:Kyl  18:Naru  19:Alex
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

#This idtoname function takes in an int 'id' and puts out a string 'name'
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

#This function takes in the order and determines if a player is dead.
def dead(order):
	stats = statslist[order]
	try:
		stats.index("Dead")
		dead = True
	except ValueError:
		dead = False
	return dead

#This function takes in the order, and determines if a player is unconscious.
def unconscious(order):
	stats = statslist[order]
	try:
		stats.index("Unconscious")
		unconscious = True
	except ValueError:
		unconscious = False
	return unconscious

#This function takes in the order, and determines if a player has surrendered.
def surrendered(order):
	stats = statslist[order]
	try:
		stats.index("Surrendered")
		surrendered = True
	except ValueError:
		surrendered = False
	return surrendered

#This function takes in the order, and determines if a player has run away.
def ranaway(order):
	stats = statslist[order]
	try:
		stats.index("Ran Away")
		ranaway = True
	except ValueError:
		ranaway = False
	return ranaway

#This marks a player who is dead, but not marked as such.
#It takes in the order, and if the player has HP lower than -10, but is not marked as dead
#It marks the player as dead.
def markasdead(order):
	global statslist
	stats = statslist[order]
	try:
		stats.index("Dead")
		marked = True
	except ValueError:
		marked = False
	if ((marked == False) and (stats[0] < -10)):
		stats.append("Dead")
		statslist[order] = stats

#This marks a player who is unconscious, but is not marked as such.
#It takes in the order, and if the player has HP between 0 and -10, but is not makred
#It marks the player as unconscious.
def markasunconscious(order):
	global statslist
	stats = statslist[order]
	try:
		stats.index("Unconscious")
		marked = True
	except ValueError:
		marked = False
	if ((marked == False) and (-10 <= stats[0]) and (stats[0] <= 0)):
		stats.append("Unconscious")
		statslist[order] = stats

#this function prints out the stats of a player from the input of his  
#order in the order list
def printstats(order):
	stats = statslist[order]
	print("Stats for " + idtoname(orderlist[order]) + ":")
	print ("Health Points: "+str(stats[0]))
	print ("Stamina: "+str(stats[1]))
	print ("Favor: "+str(stats[2]))
	print ("Ammunition: "+str(stats[3]))
	print ("Physical Attack: "+str(stats[4]))
	print ("Magical Attack: "+str(stats[5]))
	print ("Technological Attack: "+str(stats[6]))
	print ("Physical Defense: "+str(stats[7]))
	print ("Magical Defense: "+str(stats[8]))
	print ("Technological Defense: "+str(stats[9]))
	for x in range (10, len(stats)):
		print(stats[x])
	print(" ")

#This battleid fucntion is given the player's battle ID
#It outputs a list containing the Player's initial stats.
#Order of stats:
#HP, SP, FP, AP, PA, MA, TA, PD, MD, TD.
def battleid(id):
		if (id == 1):
			stats = [350, 200, 0, 50, 25, 0, 25, 20, 15, 10]
		elif (id == 2):
			stats = [220, 120, 500, 0, 24, 28, 0, 23, 18, 23]
		elif (id == 3):
			stats = [50, 300, 300, 300, 4, 4, 4, 4, 4, 4]
		elif (id == 4):
			stats = [300, 150, 200, 10, 15, 19, 1, 19, 19, 17]
		elif (id == 5):
			stats = [300, 0, 0, 0, 20, 0, 30, 25, 25, 25]
		elif (id == 6):
			stats = [250, 100, 200, 0, 10, 20, 0, 15, 25, 10]
		elif (id == 7):
			stats = [180, 30, 300, 0, 2, 30, 0, 20, 25, 20]
		elif (id == 8):
			stats = [130, 160, 260, 150, 22, 22, 22, 15, 15, 15]
		elif (id == 9):
			stats = [110,250,0,60,0,0,30,23,30,10]
		elif (id == 10):
			stats = [250, 250, 0, 0, 35, 0, 0, 20, 15, 15]
		elif (id == 12):
			stats = [150, 100, 210, 210, 10, 12, 21, 14, 14, 14]
		elif (id == 13):
			stats = [0, 0, 300, 0, 0, 30, 0, 0, 25, 0]
		elif (id == 15):
			stats = [26, 30, 300, 0, 2, 30, 0, 20, 25, 20]
		elif (id == 16):
			stats = [400, 100, 200, 0, 20, 10, 0, 20, 20, 20]
#		elif (id == 17):
		elif (id == 18):
			stats = [150, 200, 100, 0, 15, 15, 0, 15, 15, 20]
		elif (id == 19):
			stats = [150, 300, 0, 0, 25, 0, 25, 10, 20, 20]
		return stats

#this function calculates the final attack value of a physical attack.
#It takes in the order of the attacker.
def physicalattackroll(order):
	stats = statslist[order]
	roll = random.randrange(1, 21)
	print(idtoname(orderlist[order]) + " rolled " + str(roll))
	finalvalue = roll + stats[4]
	return finalvalue

#This function calculates the final attack value of a magical attack.
#It takes in the order of the attacker.
def magicalattackroll(order):
	stats = statslist[order]
	roll = random.randrange(1,21)
	print((idtoname(orderlist[order])) + " rolled " + str(roll))
	finalvalue = roll + stats[5]
	return finalvalue

#This function calculates the final attack value of a technological attack.
#It takes in the order of the attacker.
def technologicalattackroll(order):
	stats = statslist[order]
	roll = random.randrange(1, 21)
	print(idtoname(orderlist[order]) + " rolled " + str(roll))
	finalvalue = roll + stats[6]
	return finalvalue

#This function calculates the final defense value against physical damage.
#It takes in the order of the defender.
def physicaldefenseroll(order):
	stats = statslist[order]
	roll = random.randrange(1, 21)
	print(idtoname(orderlist[order]) + " rolled " + str(roll))
	finalvalue = roll + stats[7]
	return finalvalue

#This function calculates the final defense value against magical damage.
#It takes in the order of the defender.
def magicaldefenseroll(order):
	stats = statslist[order]
	roll = random.randrange(1, 21)
	print(idtoname(orderlist[order]) + " rolled " + str(roll))
	finalvalue = roll + stats[8]
	return finalvalue

#This function calculates the final defense value against technological damage.
#It takes in the order of the defender.
def technologicaldefenseroll(order):
	stats = statslist[order]
	roll = random.randrange(1, 21)
	print(idtoname(orderlist[order]) + " rolled " + str(roll))
	finalvalue = roll + stats[9]
	return finalvalue

#This function calculates if a single target attack hits
#It takes in the order of the attacker and the defender's order, the attack type and the damage type
#Physical: 1 Magical: 2 Technological: 3
#It outputs a bool variable
#If the attack hits, it outputs True
#If the attack does not hit, it outputs False
def singletargetattack(attackerorder, defenderorder, attacktype, damagetype):
	#physical attack
	if (attacktype == 1):
		atkvalue = physicalattackroll(attackerorder)
	#Magical attack
	elif (attacktype == 2):
		atkvalue = magicalattackroll(attackerorder)
	#Technological attack
	elif (attacktype == 3):
		atkvalue = technologicalattackroll(attackerorder)
	#Physical damage
	if (damagetype == 1):
		defvalue = physicaldefenseroll(defenderorder)
	#Magical damage
	elif (damagetype == 2):
		defvalue = magicaldefenseroll(defenderorder)
	#Technological damage 
	elif (damagetype == 3):
		defvalue = technologicaldefenseroll(defenderorder)
	if (atkvalue > defvalue):
		return True
	else:
		return False

#This function calculates if an AOE attack hits
#It takes in the order of the attacker and the list of all the defender's order
#The attack type and the damage type.
#It returns a list of bool variables
def aoeattack(attackerorder, defenderlist, attacktype, damagetype):
	hitlist = []
	for x in range (0, len(defenderlist)):
		temp = singletargetattack(attackerorder, defenderlist[x], attacktype, damagetype)
		hitlist.append(temp)
	return hitlist

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
		#Surrender
		if (attack == 1):
			print("You have surrendered.")
			attackerstats.append("Surrendered")
			statslist[order] = attackerstats
		elif (attack == 2):
			print("You have started to run away.")
			attackerstats.append("Running Away")
			statslist[order] = attackerstats
		#Come Hither, Technological Attack, Physical Damage.
		#10 SP
		#Genevas either grapples to somebody or grapples them to him. 
		#If the target's HP is less than Genevas's, do the latter, if not, former.
		#If the former, it deals 15 damage and prevents an escape attempt
		#If the latter, it deals 20 damage and reduces their PD and TD by 1
		elif (attack == 3):
			#if Genevas does not have enough Stamina, this attack will cancel, and the function will return False.
			if (attackerstats[1] < 10):
				print("You do not have enough Stamina to do this.")
				return False
			else:
				print("Please input the Battle ID of your target.")
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
					print("Genevas's 'Come Hither' hits " + idtoname(target) + "!")
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
		#Chemical Blood, Physical Attack, Physical Damage
		#20 SP, 25 damage
		#Roll d5, if 3, extra 10 damage and gets SP back.
		elif (attack == 4):
			#If Genevas does not have enough Stamina, this attack will cancel, and the function will return False.
			if (attackerstats[1]<20):
				print("You do not have enough Stamina to do this.")
				return False
			else:
				print("Please input the Battle ID of your target.")
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
				#You have your Battle ID of your target stored in the variable target
				targetorder = orderlist.index(target)

				targetstats = statslist[targetorder]
				#Now, you have both the attacker's stats and the target's stats.
				temp = attackerstats[1]
				temp = temp - 20
				attackerstats[1] = temp
				attackersroll = random.randrange(1, 21)
				print("Genevas rolled " + str(attackersroll) + "from a D20.")
				defendersroll = random.randrange(1, 21)
				print(idtoname(target) + " rolled " + str(defendersroll) + " from a D20.")
				finalattackvalue = attackerstats[4] + attackersroll
				print("Genevas's final attack value is " + str(finalattackvalue))
				finaldefensevalue = targetstats[7] + defendersroll
				print(idtoname(target) + "'s final defense value is " + str(finaldefensevalue))
				#When the attack hits.
				if (finalattackvalue > finaldefensevalue):
					print("Genevas's 'Chemical Blood' hits " + idtoname(target) + "!")
					#roll D5. if 3, Stamina is given back, and extra 10 damage.
					specialroll = random.randrange(1, 6)
					print("Genevas rolled " +str(specialroll) + "from a D5.")
					#When it rolls 3
					if (specialroll == 3):
						print("Genevas deals 10 extra damage and regains 20 SP!")
						#deals 35 damage
						temp = targetstats[0]
						temp = temp - 35
						targetstats[0] = temp
						#20 Stamina is given back
						temp = attackerstats[1]
						temp = temp + 20
						attackerstats[1] = temp
					#When it does not roll 3
					else:
						#deals 25 damage
						temp = targetstats[0]
						temp = temp - 25
						targetstats[0] = temp
				#When the attack does not hit.
				else:
					print("Genevas's 'Chemical Blood' did not hit" + idtoname(target)+ "!")
				statslist[order] = attackerstats
				statslist[targetorder] = targetstats
				return True

#This function calculates the effects when the player chooses to surrender
def surrender(order):
	global statslist
	stats = statslist[order]
	stats.append("Surrendered")
	print(idtoname(orderlist[order]) + " has surrendered!")

#This function calculates the effects when the player chooses to run away
def runaway(order):
	global statslist
	stats = statslist[order]
	stats.append("Running Away")
	print(idtoname(orderlist[order]) + " has started to run away!")

#This function calculates the effects when Genvas chooses to use Come Hither
#If the attack was carried out, it returns True. If the attack was not carried out for whatever reason, it returns false
#Come Hither, Technological Attack, Physical Damage.
#10 SP
#Genevas either grapples to somebody or grapples them to him. 
#If the target's HP is less than Genevas's, do the latter, if not, former.
#If the former, it deals 15 damage and prevents an escape attempt
def comehither(defenderorder):
	global statslist
	attackerorder = orderlist.index(1)
	attackerstats = statslist[attackerorder]
	defenderstats = statslist[defenderorder]
	#If Genevas doesnt have enough stamina
	if (attackerstats[1] < 10):
		print("You do not have enough stamina to do this.")
		return False
	#If Genevas has enough stamina
	else:
		hit = singletargetattack(attackerorder, defenderorder, 3, 1)
		

#This battle function is given the order of the player and the battle ID of the player.
#It asks for the attack, and calls the attacks function
def battle(order, id):
	moved = False
	#This loop loops until the player makes a valid move.
	while (moved == False):
		#Genevas
		if (id == 1):
			print("Your turn, Genvas Treeson.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (unconscious(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Run Away
			elif (ranaway(order)):
				print("You have run away, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Come Hither(3),")
				print("Chemical Blood(4), Toxin Trickery(5), Marauders Mutilation(6),")
				print("Gender Fluid Trauma(7)")
				attack = input()
				moved = attacks(id, attack, order)
		#Andy
		elif (id == 2):
			print("your turn, Andlat Einarson Josdottir.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Metal Slash(3),")
				print("Shard Blast(4), Root(5), Iron Maiden(6), Metal Toss(7), Thunder(8),")
				print("Blood Leech(9), Transfusion(10), Shank(11), Dance(12),")
				print("Shark Attack(13)")
				attack = input()
				moved = attacks(id, attack, order)
		#Christina
		elif (id == 3):
			print("Your turn, Christina Young.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), MDF grenade(3),")
				print("EMP grenade(4), Cripple(5), Hinder(6), Flight(7), Cloaking(8),")
				print("Medpack(9), Healing Artifact(10), Flashbang(11),")
				print("Energy Transfer(12), Ammunition Station(13), Taze(14),")
				print("Full On Attack(15)")
				attack = input()
				moved = attacks(id, attack, order)
		#Tor
		elif (id == 4):
			print("Your turn, Tor Ranneth.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2),")
				print("I Like Big Buffs and I Cannot Lie (3),")
				print("Rose Garden Filled With Thorns(4), Just Like Animals (5),")
				print("Rivers in the Night(6), Freedom Feels Like Flying (7),")
				print("Remember the Avocado(8), Various Nature Themed Attacks(9)")
				attack = input()
				moved = attacks(id, attack, order)
		#Ophelia
		elif (id == 5):
			print("Your turn, X01148-F Ophelia.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Beep(3), Boop(4),")
				print("Scanning(5), Short Circuit(6), Recharge(7), Terminate(8)")
				attack = input()
				moved = attacks(id, attack, order)
		#Silas
		elif (id == 6):
			print("Your turn, Silas Dent.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Shatterglass Song(3),")
				print("Song of Repair(4), Brown Note(5), Lullaby(6), Fort-Etude(7),")
				print("Dis-Chord(8), Power Play(9), Allegro Vivace(10), Sad Violin(11),")
				print("Wait for it...(12), The Silence(13), Cut Time(14)")
				attack = input()
				moved = attacks(id, attack, order)
		#Merrie
		elif (id == 7):
			print("Your turn, Nachtmerrie Verslinder.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Daydreaming(3),")
				print("Soul Wisp(4), Inner Demons(5), Goodnight!(6), Netherworld Portal(7),")
				print("Snack Time(6)")
				attack = input()
				moved = attacks(id, attack, order)
		#Vorspiel
		elif (id == 8):
			print("Your turn, Vorspiel.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2)")
				attack = input()
				moved = attacks(id, attack, order)
		#Lace
		elif (id == 9):
			print("Your turn, Lace Wunderbar.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Stun Bomb(3),")
				print("Damage Bomb(4), Smoke Bomb(5), Collateral Bomb(6), Poison Bomb(7),")
				print("Incendiary Bomb(8), Bombgel Punch(9), Pedit Medpack(10)")
				attack = input()
				moved = attacks(id, attack, order)
		#Galath
		elif (id == 10):
			print("Your turn, Galath.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Armor Shred(3),")
				print("Backstab(4), Counter(5), Deceptive Behavior(6), Playing Dirty(7),")
				print("Speed or Power(8), Spine Breaker(9)")
				attack = input()
				moved = attacks(id, attack, order)
		#Chips
		elif (id == 12):
			print("Your turn, Gratha Tro'Urn")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Arm Canon (3),")
				print("Dice Bomb (4), Blackflame (5), Seduction (6), MAGIC CARDS (7),")
				print("Bitch Slap (8), Combo Shot (9), They Call Me Chips (10),")
				print("Try Me (11), Thanks Morkin (12)")
				attack = input()
				moved = attacks(id, attack, order)
		#Tana
		elif (id ==13):
			print("Your turn, Tana.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Fire(3), Inferno(4),")
				print("Fire V2.0(5), Fuel(6), Burn Out(7)")
				attack = input()
				moved = attacks(id, attack, order)
		#Grace
		elif (id == 15):
			print("Your turn, Grace Pandora.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Forced Evolution(3),")
				print("Disease Cloud(4), Death's Remedy(5), Reconstruction Surgeon(6),")
				print("Special Plague: Halcyon Sickness(7), Special Plague: Corrosion(8),")
				print("Glacier Shell(9), Cryo Blast(10), Frost Enchant(11),")
				print("Frost Implosion(12), Vortex(13)")
				attack = input()
				moved = attacks(id, attack, order)
		#Vant
		elif (id == 16):
			print("Your turn, Vant Copil.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2), Swing(3), Charging(4),")
				print("Aiming Practice(5), It's Mine(6), Punching(7), I'll be There for You(8).")
				attack = input()
				moved = attacks(id, attack, order)
		#Kyl
		elif (id == 17):
			print("Your turn, Kyl Sunder.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Moves: Surrender(1), Run Away(2)")
				attack = input()
				moved = attacks(id, attack, order)
		#Naru
		elif (id == 18):
			print("Your turn, Naru.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Available Attacks: Surrender(1), Run Away(2)")
				attack = input()
				moved = attacks(id, attack, order)
		#Alex
		elif (id == 19):
			print("Your turn, Alexander Claus.")
			#Dead
			if (dead(order)):
				print("You are dead, and cannot move.")
				moved = True
			#Unconscious
			elif (dead(order)):
				print("You are unconscious, and cannot move.")
				moved = True
			#Surrendered
			elif (surrendered(order)):
				print("You have surrendered, and cannot move.")
				moved = True
			#Moves
			else:
				print("Surrender(1), Run Away(2), Downward Strike(3), Low Thrust(4),")
				print("Backhand(5), Forward Knee(6), Hammer Down(7), Power Stab(8),")
				print("Disabler(9), Scapula Fracture(10), Tibia Fissure(11).")
				attack = input()
				moved = attacks(id, attack, order)


#This attack does all the phase effects for a player
#It takes in the order of the player.
def phaseeffects(order):
	global statslist
	

def endphase(order):
	global statslist

print("Welcome to the Gythian Civil War Battle Simulator.")
print("Please input the number of players.")
players = int(input())

#The orderlist contains all the battle ID of the characters in the  
#battle, in order of battle phase
orderlist = []
#The statslist contains all the stats list of all the characters in  
#battle, in order of battle phase
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
	#There are as many phases as there are players, plus an extra end  
	#phase coded seperate of this for loop.
	for x in range(0, players):
		print("Turn " + str(i)+ " Phase " + str(x + 1))
		#This loop prints the stats of all players.
		for y in range(0, players):
			printstats(y)
		#This function should take care of all the moves in this phase.
		battle(x, orderlist[x])
		#this phaseeffects function should take care of all the effects
		for y in range (0, players):
			phaseeffects(y)

	#this part codes for the end phase.
	print("Turn " + str(i)+ " End Phase")
	for y in range(0, players):
		#this loop prints the stats of all players in the end phase
		printstats(y)
	#for z in range(0, players):
		#this loop runs the end phase effects for all players
		#endphase(z)
