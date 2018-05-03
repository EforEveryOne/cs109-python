import time
from random import randint


def start():
	start = ""
	name = ""
	age = ""
	while (start) != "yes" or "no":
		start = input("Do you want to go on an adventure? ").lower()
		if "yes" in (start):
			print ("You are about to embark on your very own adventure! ")
			# time.sleep(2)
			print ("But first lets get a good look at ya. \n")
			# time.sleep(2)
			print ("CHARACTER CREATION: ")
			name = input("So you're an adventurer, eh? What is your name? ")
			print("Hmm...")
			# time.sleep(2)
			print (str(name).capitalize() + "? ")
			# time.sleep(2)
			print("That's a funny sounding name.")
			# time.sleep(3)
			while type(age) != int or type(age) != float:	
				try:
					age = int(input("How old are you? "))
					age = int(age)
					# passing in age and name into the next function because it needs their information
					input_age(age, name)
					break
				except ValueError:
					print("Be clear with me. Tell me a number! ")
			break
		elif "no" in (start):
			print("If you don't want an adventure it won't be fun anyways. \nThe End. ")
			break
		else:
			print("Be clear with me. Yes or no. Don't complicate things! ")
			# time.sleep(1.5)

# First called function but calls the func input_class
# takes user input age and determines impacts gameplay and dialogue
def input_age(age, name):
# crossroads of age choice
	if age <= 0: 
		print (str(age) + "? ")
		# time.sleep(2)
		print ("You're not even born yet... Come back when you exist. \nThe End. ")
	# 1-8
	elif age <= 8:
		print (str(age) + "? ")
		# time.sleep(2)
		print ("You are too young too young for this adventure. Go take a nap, kid. \nThe End. ")
	# 9-16
	elif age <= 16:
		print (str(age) + "? ")
		# time.sleep(2)
		print ("? You are rather young. But you can make it with some luck. ")
		strength = 4
		endurance = 4
		input_class(age, name, endurance, strength)
	# 17-30
	elif age <= 30:
		print(str(age) + "? ")
		# time.sleep(2)
		print("You've got some experience but there's an entire world left to explore.")
		strength = 8
		endurance = 8
		input_class(age, name, endurance, strength)
	# 31-60
	elif age <= 60:
		print(str(age) + "? ")
		# time.sleep(2)
		print("You're not as young as you once were but you've got experience and know your way around the world.")
		strength = 6
		endurance = 6
		input_class(age, name, endurance, strength)
	# 61-80
	elif age <= 80:
		print(str(age) + "? ")
		# time.sleep(2)
		print("Wow. You are at the end of your days... This is probably your last adventure. Lets make it good!")
		strength = 2
		endurance = 2
		input_class(age, name, endurance, strength)
	# 81+
	elif age >= 81:
		print(str(age) + "? ")
		# time.sleep(2)
		print("You are too old! You already had your adventure. Go take a nap. \nThe End. ") 

# Takes in previous inputs and continues to gather more info about the player, building the character
def input_class(age, name, endurance, strength):
	char_class = ""
	# time.sleep(4)
	print("Tell me...")
	# time.sleep(3)
	while (char_class) != "defensive" or "aggressive":
		char_class = input("Do you consider yourself more of a Defensive or an Aggressive person? ").lower()
		if "defensive" in (char_class):
			char_class = "Tank"
			endurance += 5
			# time.sleep(2)
			print ("Congratulations. Your character is complete. \nYou are ready for adventure! \n\n")
			# time.sleep(2)
			calc_stats(age, name, endurance, strength, char_class)
			break
		elif "aggressive" in (char_class):
			char_class = "Fighter"
			strength += 5
			# time.sleep(2)
			print ("Congratulations. Your character is complete. \nYou are ready for adventure! \n\n")
			# time.sleep(2)
			calc_stats(age, name, endurance, strength, char_class)
			break
		else:
			print("Be clear with me. Defensive or an Aggressive? ")
			# time.sleep(0.5)

# Googled around looking for a clear console function, simplest method was:
# print("\n" * 50)
# I took the idea and put it into a customizable loop
# Utility function to "clean" old text clutter in the console
def clear(amount):
	i = 0
	for i in range(amount):
		time.sleep(1)
		print("\n")
		i += 1
	
# Compiles all the player info gathered in the previous functions
def calc_stats(age, name, endurance, strength, char_class):
	attribute_points = 0
	level = 1
	max_hitpoints = endurance * 2 + level
	current_hitpoints = max_hitpoints
	damage = strength / 2 + level
	damage = int(damage)
	armor = 0
	gold = age / 3
	gold = int(gold)
	current_experience = 0
	next_level_exp = 100 + current_experience * 2
	inventory = []
	is_weapon_slot_filled = 0
	is_armor_slot_filled = 0
	current_weapon = "None"
	current_armor = "None"

	# Creates the player_character class object and passes in all the vars at their custom inputs.
	# will need to change player hipoints to a max hitpoints and a current hitpoints.
	class player_character:
		def __init__(self, name, age, char_class, endurance, strength, current_hitpoints, max_hitpoints,
			         damage, armor, level, attribute_points, current_experience, next_level_exp, gold, inventory,
			         is_weapon_slot_filled, is_armor_slot_filled, current_weapon, current_armor):
			self.name = name
			self.age = age
			self.char_class = char_class
			self.endurance = endurance
			self.strength = strength
			self.current_hitpoints = current_hitpoints
			self.max_hitpoints = max_hitpoints
			self.damage = damage
			self.armor = armor
			self.level = level
			self.attribute_points = attribute_points
			self.current_experience = current_experience
			self.next_level_exp = next_level_exp
			self.gold = gold
			self.inventory = []
			self.is_weapon_slot_filled = is_weapon_slot_filled
			self.is_armor_slot_filled = is_armor_slot_filled
			self.current_weapon = current_weapon
			self.current_armor = current_armor

		# Character sheet (player information).
		def details(self):
			print("CHARACTER SHEET: \nName: " + str(self.name).capitalize() + ". \nAge: " + str(self.age) +
				  ". \nClass: " + str(self.char_class) + ". \nEndurance: " + str(self.endurance) +
				  ". \nStrength: " + str(self.strength) + ". \nHitpoints: " + str(self.current_hitpoints) +
				  "/" + str(self.max_hitpoints) + ". \nDamage: " + str(self.damage) + ". \nArmor: " +
				  str(self.armor) + ". \nLevel: " + str(self.level) + ". \nAttribute Points: " +
				  str(self.attribute_points) + ". \nCurrent Experience: " + str(self.current_experience) + 
				  ". \nExp to next Level: " + str(self.next_level_exp) + ". \nGold: " + str(self.gold) + 
				  ". \nCurrent Weapon: " + str(self.current_weapon) + ". \nCurrnet Armor: " + 
				  str(self.current_armor) + ". \nInventory: " + str(self.inventory))
			clear(1)

		def inventory_management(self):
			print("huh")

	# Make the player global to give full scope access to the rest of the functions that rely on it.
	global player
	# Create the player with all the required information gathered in the previous functions.
	player = player_character(name, age, char_class, endurance, strength, current_hitpoints, max_hitpoints,
							  damage, armor, level, attribute_points, current_experience, next_level_exp,
							  gold, inventory, is_weapon_slot_filled, is_armor_slot_filled, current_weapon,
							  current_armor)
	player.details()
	# time.sleep(6)
	# clear(1)
	print("\nI wish you well on your adventure, " + (player.name) + "!") 
	# clear(1)
	# time.sleep(2)
	print(" \n\nYour eyes are getting heavy...")
	# clear(1)
	# time.sleep(2)
	print("Your vision is blurry...")
	# clear(1)
	# time.sleep(2)
	print("The wolrd fades away...")
	# time.sleep(4)
	print("\n" * 50)
	# time.sleep(3)
	print("You wake up on a dusty road.")
	town_first_visit()
	# return player


# Creating object group for armor
class armor():
	"""docstring fos armor"""
	def __init__(self, name, level_requirment, armor_bonus):
		self.name = name
		self.armor_bonus = armor_bonus
		self.level_requirment = level_requirment

	def equip_item(self, player):
		if player.level < self.level_requirment:
			print("Your level is too low. \nYour level: " + str(player.level) +
				  ". \n" + "Item level: " + str(self.level_requirment) + ". ")
		elif player.is_armor_slot_filled == 1:
			print("You already have armor. " + "Current Armor: " + str(player.current_armor))
		elif (self.name) in player.inventory:
			player.inventory.remove (self.name)
			player.armor += self.armor_bonus
			player.is_armor_slot_filled = 1
			player.current_armor = str(self.name)
		else:
			player.armor += self.armor_bonus
			player.is_armor_slot_filled = 1
			player.current_armor = str(self.name)
			
	def unequip_item(self, player):
		if player.is_armor_slot_filled == 0:
			print("You aren't wearing any armor. ")
		elif player.is_armor_slot_filled == 1:
			player.armor -= self.armor_bonus
			player.is_armor_slot_filled = 0
			player.current_armor = "None"
			player.inventory.append (self.name)

# Creating object group for weapons
class weapon_class():
	"""docstring for weapon"""
	def __init__(self, name, level_requirment, damage_bonus):
		self.name = name
		self.damage_bonus = damage_bonus
		self.level_requirment = level_requirment

	def equip_item(self, player):
		if player.level < self.level_requirment:
			print("Your level is too low. \nYour level: " + str(player.level) +
				  ". \n" + "Item level: " + str(self.level_requirment) + ". ")
		elif player.is_weapon_slot_filled == 1:
			print("You already have a weapon. " + "Current Weapon: " + str(player.current_weapon))
		elif (self.name) in player.inventory:
			player.inventory.remove (self.name)
			player.damage += self.damage_bonus
			player.is_weapon_slot_filled = 1
			player.current_weapon = str(self.name)
		# Putting armor on for the first time (can't remove it from inventory).
		# Maybe can fix by adding to inventory when found, that can happen when more features are added. 
		else:
			player.damage += self.damage_bonus
			player.is_weapon_slot_filled = 1
			player.current_weapon = str(self.name)
			
	def unequip_item(self, player):
		if player.is_weapon_slot_filled == 0:
			print("You aren't wielding a weapon. ")
		elif player.is_weapon_slot_filled == 1:
			player.damage -= self.damage_bonus
			player.is_weapon_slot_filled = 0
			player.current_weapon = "None"
			player.inventory.append (self.name)

	def weapon_details(self):
		print("Weapon details: " + "\nName: " + str(self.name) + ". \nLevel Required: " +
			  str(self.level_requirment) + ". \nDamage: " + str(self.damage_bonus) + ". \n")

# need to add a create armor and weapon function that can be dropped as loot. How to randomize the name?

# chance of a weapon was rolled after defeating an enemy already, if it succeeded, this is called
def roll_weapon_reward():
	roll = randint(0,100)
	print(roll)
	if roll <= 60:
		weak_sword()
	elif roll <= 90:
		average_sword()
	elif roll <= 99:
		super_sword()
	elif roll == 100:
		best_sword()


def weak_sword():
	# weapon = 1
	global weapon
	weapon = weapon_class("Weak Sword", 1, randint(1,4))
def average_sword():
	global weapon
	weapon = weapon_class("Average Sword", randint(1,4), randint(4, 10))
	print(weapon)
	# player.inventory.append (weapon)
	player.inventory.append (weapon.name)

	player.details()
	weapon.weapon_details()
	weapon.equip_item(player)
	player.details()
def super_sword():
	global weapon
	weapon = weapon_class("Super Sword", randint(10,15), randint(10,20))
def best_sword():
	global weapon
	weapon = weapon_class("Best Sword", randint(20,30), randint(100,200))


# testweapon = weapon("A good stick", 0, 10)
# super_test_weapon = weapon("Dragon Slayer", 10, 50)

# testarmor = armor("Leather Armor", 0, 10)
# super_test_armor = armor("Shavs Wrap", 10, 50)




class enemy_class():
	def __init__(self, name, hitpoints, damage, armor, experience_reward, gold):
		self.name = name
		self.hitpoints = hitpoints
		self.damage = damage
		self.armor = armor
		self.experience_reward = experience_reward
		self.gold = gold

def spawn_wolf():
	global enemy
	enemy = enemy_class("Wolf", randint(5,12), randint(1,3), randint(0,1), randint(10,30), randint(0,1))
def spawn_bandit():
	global enemy
	enemy = enemy_class("Bandit", randint(10,20), randint(4,10), randint(0,3), randint(50,100), randint(0,20))
def spawn_troll():
	global enemy
	enemy = enemy_class("Troll", randint(20,50), randint(5,15), randint(2,10), randint(500,1000), randint(20,50))
def spawn_dragon():
	global enemy
	enemy = enemy_class("Dragon", randint(1000,2000), randint(50,100), randint(20,50), randint(10000,30000), randint(1000,3000))



# need to add level up print text and time.sleep for the player to see it before moving back
# to the game and their choice input
def level_up_check(player):
	# fill up with print statments, figure out what's wrong.
	if player.current_experience >= player.next_level_exp:
		cross_over_experience = player.current_experience - player.next_level_exp
		player.level += 1
		player.attribute_points +=2
		# total_experience += current_experience
		player.next_level_exp = float(player.next_level_exp)
		player.next_level_exp = player.current_experience ** 1.2 / 2
		player.next_level_exp = int(player.next_level_exp)
		player.current_experience += cross_over_experience
		# calling the function because it's supposed to loop through itself, leveling the player up
		# as long as they have an overflow of xp required for the next level.
		# need to fix up the logic.
		level_up_check(player)
	else:
		return
		# player.current_experience = 0



# BEFORE CALLING THIS FUNCTION CHECK IF THEY HAVE ATTRIBUTE POINTS > 0
def spend_attributes():
	player.attribute_points +=10
	print("\nUnspent points: " + str(player.attribute_points) + "Current \nStrength: " 
		  + str(player.strength) + "\nCurrent Endurance: " + str(player.endurance))
	action = ""
	spend = ""
	clear(1)
	print("Available Commands: \nSTRENGTH - increase strength \nENDURANCE - increase endurance \nCANCEL - go back ")

	while action != "strength" or "endurance" or "cancel":
		action = input(str(player.name) + ": ").lower()
		# action = input("Spend Points on strength or endurance? ").lower()
		if "strength" in action:

			player.attribute_points 
			while type(spend) != int:
				try:
					spend = int(input("How many points do you wish to spend? "))
				except ValueError:
					print("Please input a number. ")
			if spend > player.attribute_points:
				print("You don't have that many attribute points! ")
				break
			elif player.attribute_points <= spend:
				player.strength += spend
				break


		elif "endurance" in action:
			while type(spend) != int:
				try:
					spend = int(input("How many points do you wish to spend? "))
				except ValueError:
					print("Please input a number. ")
			if spend > player.attribute_points:
				print("You don't have that many attribute points! ")
				break
			elif player.attribute_points <= spend:
				player.endurance += spend
				break
				
		elif "no" in action:
			print("Not spending any points and leaving the spend_attributes function ")
			break
		else:
			break
		break



# need to add while loop to for command input
def church():
	action = ""
	heal_cost = player.level + 10
	print("You entered the church and are greeted by a preist. ")
	time.sleep(1)
	print("Preist: 'Do you want to be healed?' ")
	time.sleep(1)
	print("Preist: 'It only costs " + str(heal_cost) + " gold for you.' ")
	time.sleep(1)
	print("Current gold: " + str(player.gold) + ". ")
	while action != "yes" or "no":
		action = input(str(player.name) + ": ").lower()
		if "yes" in action:
				if player.gold >= heal_cost:
					player.gold -= heal_cost
					clear(1)
					print("Current HP: " + str(player.current_hitpoints) + "/" + str(player.max_hitpoints))
					heal_amount = player.max_hitpoints - player.current_hitpoints
					player.current_hitpoints += heal_amount
					print("The priest is tending to your wounds... ")
					clear(3)
					print("You recovered " + str(heal_amount) + "HP. ")
					print("\nCurrent HP: " + str(player.current_hitpoints) + "/" + str(player.max_hitpoints))
					print("Current gold: " + str(player.gold))
					clear(2)
					town()
				elif player.gold < heal_cost:
					clear(1)
					print("You don't have enough gold. But Please come back when you do.")
					clear(2)
					town()
		elif "no" in action:
			print("Preist: 'Maybe next time...' \nYou leave the church. \n")
			clear(2)
			town()
		else:
			print("Priest: 'Sorry, I'm hard of hearing. Did you say yes or no?")



def town():
	action = ""
	print("You enter the town center. ")
	clear(1)
	print("Available Commands: \nSHOP - buy and sell items. \nCHURCH - recover hitpoints " +
		  "\nWILDERNESS - fight enemies \nPLAYER - inventory, equipment management, skill points ")
	clear(1)
	while (action) != "shop" or "church" or "wilderness" or "player":
		action = input(str(player.name).capitalize() + ": ").lower()
		clear(1)

		if "shop" in action:
			shop()
			break
		elif "church" in action:
			church()
			break
		elif "wilderness" in action:
			wilderness()
			break
		elif "player" in action:
			player.details()

			# print(str(player.inventory))
			print("Available Commands: \nEQUIP \nUNEQUIP \nCANCEL \n")
			sub_action = input(str(player.name) + ": ").lower()
			clear(1)
			if "equip" in sub_action:
				equip_an_item()
				break
			elif "unequip" in sub_action:
				unequip_an_item()
			elif "cancel" in sub_action:
				break
			else:
				break
			break
		else:
			print(" \nYou are in the town center. \nAvailable Commands: \nSHOP \nCHURCH \nWILDERNESS \nPLAYER ")


# subset of commands that allows the play to swap out their equipment and spend skillpoints. and eventually use items
def player_command():
	print("placeholder ")



# Can do it by passing in arguments instead but need to keep track of them between transitions
# (requires having other areas built)
# first_visit = 1
def town_first_visit():
	print("first town visit, introduction ")
	# print("now sending the player to the normal town. You can visit the Shop, the Church, the Wilderness, or check your supplies. ")
	# Have the player test combat by getting in a fight with a drunk person, the player
	# has no weapons yet so tey won't kill them.
	# The townspeople congratulate the player
	# introduce player to the church that heals them.
	# introduce the player to the shop
	# shop will tell them about the wilderness
	# player leaves the shop and goes to the "main square"
	# this is where the player takes control.
	# They can examine their player details, that means, stats, inventory, 
	# They can head to the church, shop, or wilderness.
	town()

def wilderness():
	action = ""
	print("You are in the wilderness! ")
	print("You can use the following commands: \n\nEXPLORE - fight enemies \nTOWN - leave wilderness " + 
		  "\nPLAYER - inventory, equipment management, skill points ")
	
	while action != "explore" or "town" or "player":
		action = input(str(player.name).capitalize() + ": ").lower()
		if "explore" in action:
			print("You wander around the wilderness... ")
			clear(4)
			encounter(player)
			break
		elif "town" in action:
			print("Travelling back to town... ")
			clear(4)
			town()
			break
		elif "player" in action:
			player_command()
			break
		else:
			print("Invalid Command ")
			clear(1)



	encounter(player)
	# print("\nWhat do you want to do? \n\nYou can head back to town or explore the wilderness!")
	# make a loop asking for text input, that will run a function:
	# explore the wilderness more (encounter)
	# Go back to town (from there you'll have the same kind of setup but different functions, like shop)
	# character details
	# spend attribute points.
	# item access, manage equipment
	# 




def bad_end():
	print("You are dead. Game over. ")
	print("this is in the function bad_end")

def players_turn(player, enemy, run_away):
	print("================================= \n" + (player.name).capitalize() +
		  "'s TURN: \nYou can use the following commands: \nATTACK \nRUN \nITEM\n ")
	if run_away == 0:
		if player.current_hitpoints <= 0:
			# print("calling bad_end function fron players_turn 'if player.current_hitpoints <= 0")
			bad_end()
		elif enemy.hitpoints <= 0:
			# print("the enemy hp is not greater than 0, they should be dead. this is printed inside players_turn")
			print("You defeated the " + str(enemy.name) + "! ")
			player.current_experience += enemy.experience_reward
			player.gold += enemy.gold
			level_up_check(player)
		elif enemy.hitpoints >= 1:
			# print("the enemy hp is greater than 1, so move onto player turn input 'action'")
			action = ""
			while action != "attack" or "run" or "item":
				action = input(str(player.name).capitalize() + ": ").lower()
				if "attack" in (action):
					combat_damage = player.damage
					combat_damage -= enemy.armor
					if combat_damage > 0:
						enemy.hitpoints -= combat_damage
						clear(1)
						print("You struck the enemy for " + str(combat_damage) + " damage after " + str(enemy.armor) +
							  " was blocked by their armor! ")
						if enemy.hitpoints >= 1:
							# clear(1)
							print("================================= \n")
							time.sleep(3)
							enemy_turn(player, enemy, run_away)
							break
						# check if enemy is dead
						else:
							clear(1)
							print("You defeated the " + str(enemy.name) + "! ")
							player.current_experience += enemy.experience_reward
							level_up_check(player)
							break
					else:
						clear(1)
						print("The " + str(enemy.name) + "'s armor is too high! ")
						# clear(1)
						print("================================= \n")
						enemy_turn(player, enemy, run_away)
						break
				elif "run" in (action):
					clear(1)
					run_chance = randint(1,100)
					print("You attempt to run away: \nYou rolled: " + str (run_chance) + " out of 100. ")
					if player.age <= 16:
						if run_chance <= 90:
							run_away = 1
							# print("run_away is set to: " + str(run_away) + "You should run away and leave combat.")
							print("You succesfully escaped the " + str(enemy.name) +
								  "! \n================================= \n")
							break
						else:
							run_away = 0
							# print("run_away is set to: " + str(run_away) + "You should not be able to run away.")
							print("The " + str(enemy.name) + " prevented you from escaping! \n")
							enemy_turn(player, enemy, run_away)
							break
					elif player.age <= 30:
						if run_chance <= 50:
							run_away = 1
							# print("run_away is set to: " + str(run_away) + "You should run away and leave combat.")
							print("You succesfully escaped the " + str(enemy.name) +
								  "! \n================================= \n")
							break
						else:
							run_away = 0
							# print("run_away is set to: " + str(run_away) + "You should not be able to run away.")
							print("The " + str(enemy.name) + " prevented you from escaping! \n")
							enemy_turn(player, enemy, run_away)
							break
					elif player.age <= 60:
						if run_chance <= 30:
							run_away = 1
							# print("run_away is set to: " + str(run_away) + "You should run away and leave combat.")
							print("You succesfully escaped the " + str(enemy.name) +
								  "! \n================================= \n")
							break
						else:
							run_away = 0
							# print("run_away is set to: " + str(run_away) + "You should not be able to run away.")
							print("The " + str(enemy.name) + " prevented you from escaping! \n")
							enemy_turn(player, enemy, run_away)
							break
					elif player.age <= 80:
						if run_chance <= 10:
							run_away = 1
							# print("run_away is set to: " + str(run_away) + "You should run away and leave combat.")
							print("You succesfully escaped the " + str(enemy.name) +
								  "! \n================================= \n")
							break
						else:
							run_away = 0
							# print("run_away is set to: " + str(run_away) + "You should not be able to run away.")
							print("The " + str(enemy.name) + " prevented you from escaping! \n")
							enemy_turn(player, enemy, run_away)
							break
					# run(player, enemy)
					# break
				# elif "item" in (action):
				# 	# loop through actons with items can take off an item, but need to equip an item.
				# 	print(player.inventory)
				# 	item_action = input("use, item name ")
				# 	# if item_action = How to check for weapon/armor/or other item?
				# 	break
				else:
					# infinite loop happens here. Why?
					print("Please type 'attack' 'run' or 'item' into the console. ")
		else:
			print("You successfully ran away! - players_turn function")
			wilderness()



def enemy_turn(player, enemy, run_away):
	# If run away is not true, continue the fight
	if run_away == 0:
		if player.current_hitpoints <= 0:
			# print("calling bad_end function fron enemy_turn 'if player.current_hitpoints <= 0")
			bad_end()
			# break
		elif enemy.hitpoints >= 1:
			print("================================= \nENEMY TURN:")
			combat_damage = enemy.damage
			combat_damage -= player.armor
			if combat_damage > 0:
				player.current_hitpoints -= combat_damage
				print("The " + str(enemy.name) + " hit you for " + str(combat_damage) + " damage after " + str(player.armor) +
					  " was blocked by your armor!")
				print("Player HP: " + str(player.current_hitpoints) + "/" + str(player.max_hitpoints))
				# clear(2)
				# check if player is dead
				if player.current_hitpoints <= 0:
					# print("calling bad_end function fron enemy_turn, after player took dmg from enemy")
					print("================================= \n")
					bad_end()
					# break
				else:
					print("================================= \n")	
					players_turn(player, enemy, run_away)
			else:
				print("Your armor protects you from the " + str(enemy.name) + "! ")
				players_turn(player, enemy, run_away)
		else:
			print("the enemy should be dead!")
			player.details()
	else:
		print("the player should have ran away!")
		player.details()
	
def create_random_enemy():
	# spawn a randomized enemy
	randomize_spawn = randint(1,100)
	if randomize_spawn <= 50:
		spawn_wolf()
	elif randomize_spawn <= 90:
		spawn_bandit()
	elif randomize_spawn <= 99:
		spawn_troll()
	elif randomize_spawn == 100:
		spawn_dragon()
# encounter determines who goes first, and spawns the enemy,
# pass in the arguments required (the player, and enemy, run_away)
def encounter(player):
	"""encounter is the function that initiates combat. encounter determines turn order and enemy type"""
	run_away = 0
	# Create a randomized enemy.
	create_random_enemy()
	print("\nA " + str(enemy.name) + " has appeared! \n")

	# Decide who goes first.
	turn_order = randint(1,100)
	print("Deciding turn order...")
	time.sleep(2)
	print("You rolled: " + str(turn_order) + " out of 100. ")
	time.sleep(2)

	if player.age <= 16:
		if turn_order <= 90:
			player_first = 1
		else:
			player_first = 0
	elif player.age <= 30:
		if turn_order <= 50:
			player_first = 1
		else:
			player_first = 0
	elif player.age <= 60:
		if turn_order <= 35:
			player_first = 1
		else:
			player_first = 0
	elif player.age <= 80:
		if turn_order <= 20:
			player_first = 1
		else:
			player_first = 0
	
	# Check who goes first.
	if player_first == 0:
		print("The " + str(enemy.name) + " takes action before you can react! \n")
		enemy_turn(player, enemy, run_away)
	elif player_first == 1:
		print("You're able to act before the " + str(enemy.name) + " realizes! \n")
		players_turn(player, enemy, run_away)
	# Combat is over! Back to the wilderness
	print("The encouter is over! ")
	# clear(50)
	wilderness()





# rough outline for shop in the town scene
# if player.gold >= item__shop_price:
	# player.gold -= item__shop_price:
	# player.inventory.append (self.name)