import time
from random import randint
# print(randint(0, 9))

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
			time.sleep(1)

# Utility function to "clean" console
def clear(amount):
	i = 0
	for i in range(amount):
		time.sleep(0.07)
		print("\n")
		i+=1
	
# Compiles all the player info gathered in the previous functions
def calc_stats(age, name, endurance, strength, char_class):
	attribute_points = 0
	level = 1
	hitpoints = endurance * 2 + level
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
	class player_character:
		def __init__(self, name, age, char_class, endurance, strength, hitpoints, damage, armor,
				     level, attribute_points, current_experience, next_level_exp, gold, inventory,
			         is_weapon_slot_filled, is_armor_slot_filled, current_weapon, current_armor):
			self.name = name
			self.age = age
			self.char_class = char_class
			self.endurance = endurance
			self.strength = strength
			self.hitpoints = hitpoints
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
				  ". \nStrength: " + str(self.strength) + ". \nHitpoints: " + str(self.hitpoints) +
				  ". \nDamage: " + str(self.damage) + ". \nArmor: " + str(self.armor) + ". \nLevel: " + str(self.level) +
				  ". \nAttribute Points: " + str(self.attribute_points) + ". \nCurrent Experience: " +
				  str(self.current_experience) + ". \nExp to next Level: " + 
				  str(self.next_level_exp) + ". \nGold: " + str(self.gold) + ". \nCurrent Weapon: " + str(self.current_weapon) + 
				  ". \nCurrnet Armor: " + str(self.current_armor) + ". ")

	# How else to allow the class object global scope?
	global player
	# Create the player with all the required information.
	player = player_character(name, age, char_class, endurance, strength, hitpoints, damage, armor, level,
		                      attribute_points, current_experience, next_level_exp, gold, inventory,
		                      is_weapon_slot_filled, is_armor_slot_filled, current_weapon, current_armor)
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
	print("\n" * 40)
	# time.sleep(3)
	print("You wake up on a dusty road.")
	# town()
	# return player

# Can do it by passing in arguments instead but need to keep track of them between transitions
# (requires having other areas built)
first_visit = 1
def town():
	# global first_visit
	# global first_meeting
	if first_visit == 1:
	# if first_meeting == True:
		print("Welcome to town, traveller! ")
		first_visit = 0
	# while True:

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
class weapon():
	"""docstring fos weapon"""
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


testweapon = weapon("A good stick", 0, 10)
super_test_weapon = weapon("Dragon Slayer", 10, 50)

testarmor = armor("Leather Armor", 0, 10)
super_test_armor = armor("Shavs Wrap", 10, 50)



class enemy():
	def __init__(self, name, hitpoints, damage, armor, experience_reward):
		self.name = name
		self.hitpoints = hitpoints
		self.damage = damage
		self.armor = armor
		self.experience_reward = experience_reward

def spawn_wolf():
	global wolf
	enemy = enemy("Wolf", randint(5,12), randint(1,3), randint(0,1), randint(10,30))
	print("wolf")

def spawn_bandit():
	global bandit
	enemy = enemy("Bandit", randint(10,20), randint(4,10), randint(0,3), randint(50,100))
	print("bandit")

def spawn_troll():
	global troll
	enemy = enemy("Troll", randint(20,50), randint(5,15), randint(2,10), randint(500,1000))
	print("troll")

def spawn_dragon():
	global dragon
	enemy = enemy("Dragon", randint(1000,2000), randint(50,100), randint(20,50), randint(10000,30000))
	print("dragon")



# working on this 
def players_turn(player, enemy):
	print("It's your turn! \nattack, run, item")
	while action != "attack" or "run" or "item"
		action = input("What is your move?")
		if "attack" in (action):
			# deal player damage to enemy hp,
		if "run" in (action):
			# break. get out of combat, chance the monster will get a free attack
		if "item" in (action):
			# loop through actons with items can take off an item, but need to equip an item.
			print(player.inventory)
			item_action = input("use, item name")
			# if item_action = How to check for weapon/armor/or other item?



def enemy_turn(player, enemy):




def combat(player, enemy):
	while enemy hp >= 1:
		if player_first == 1:
			players_turn(player, enemy)
			# option, run away, attack, use/swap items, go to enemy turn
		else:
			enemy_turn(player, enemy)
			# attack the player, maybe add abilities for each enemy

		# (if player dies, endgame)
		# if enemy dies, player gains exp, check lvl up.
		# end loop, back to wilderness scene


		



# encounter determines who goes first, and spawns the enemy,
# then calls the combat function based on who is going first.
# pass in the arguments required (the player, and enemy)
def encounter(player):
	turn_order = randint(1,100)
	print(turn_order)
	global player_first
	
	player_first = 0

	if player.age <= 16:
		player_first = 0
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
		if turn_order <= 30:
			player_first = 1
		else:
			player_first = 0
	elif player.age <= 80:
		if turn_order <= 10:
			player_first = 1
		else:
			player_first = 0

	print(player_first)
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

		# battle scene
		combat(player, enemy):





# need to add town scene, heals + shop



# # testing list for inventory.
# player_inventory = ["testString"]
# # player_inventory.append testweapon
# def inventory():
# 	player_inventory.append ("testString2")
# 	player_inventory.append (testarmor)
# 	player_inventory.append (player_inventory)
# 	print(player_inventory)



# equipment[]
# want to have an inventory that can be called that lists every item you have in your inventory.
# list for equipment, too?
# currency exchange
# 1 gold 10 silver 100 copper
# take in user input pick the currency type you want to exchange,
# user input how much of which currency are you giving them?
# is it valid?

# what features will you add by the final, on may 4th?
# 1. Town/base of operations - buy+sell shop, healing(costs money) - also allows to go to exploring(combat).
#  - also functional level ups
#  - In the town, be able to call functional commands, can view character sheet,
# 3. Combat.
# 5. Shop.
# level up funcationality, attribute point spending.



# level up
# to be placed after wherever exp is gained to check for level up
# def level_up(player.level, player.current_experience, player.attribute_points, player.next_level_exp):
# 	level
# 	current_experience
# 	next_level_exp
# 	attribute_points
# # level up process, level increase, attribute points to spend, set exp for next level
# 	level += 1
# 	attribute_points += 2
# 	current_experience = 0
# 	next_level_exp = 100 + current_experience * 2


# edge cases are infreuqnet/unexpected conditions which might happen due to user input.
# Like putting a string into an input that wants an int.
# Test your code for edge cases.
# account for everything if possible.
# can be used in cyber security. (like user putting in dangerous code)
#  code use the stack
# pytest is something I can use pip to install for streamline tests for functions.