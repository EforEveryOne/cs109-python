import time


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
		strength = 7
		endurance = 7
		input_class(age, name, endurance, strength)
	# 31-60
	elif age <= 60:
		print(str(age) + "? ")
		# time.sleep(2)
		print("You're not as young as you once were but you've got experience and know your way around the world.")
		strength = 5
		endurance = 5
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
	while (char_class) != "tank" or "aggressive":
		char_class = input("Do you consider yourself more of a Tank or an Aggressive person? ").lower()
		if "tank" in (char_class):
			endurance += 5
			# time.sleep(2)
			print ("Congratulations. Your character is complete. \nYou are ready for adventure! \n\n")
			# time.sleep(2)

			# print("Your name is: " + str(name).capitalize() + "\nYour age is: " + str(age) + "\nYour class is: " + str(char_class).capitalize())
			calc_stats(age, name, endurance, strength, char_class)
			# character_sheet()
			# inventory()
			break
		elif "aggressive" in (char_class):
			strength += 5
			# time.sleep(2)
			print ("Congratulations. Your character is complete. \nYou are ready for adventure! \n\n")
			# time.sleep(2)
			# print("Your name is: " + str(name).capitalize() + "\nYour age is: " + str(age) + "\nYour class is: " + str(char_class).capitalize())
			calc_stats(age, name, endurance, strength, char_class)
			# character_sheet()
			# inventory()
			break
		else:
			print("Be clear with me. Tank or an Aggressive? ")
			time.sleep(1)

# TODO
# create a for loep so you can call exaclty how many times you want it to run.

def clear(amount):
	i = 0
	for i in range(amount):
		time.sleep(0.2)
		print("\n")
		i+=1
	


# Compiles all the player info gathered in the previus functions
# creates the player_character class object and passes in all the vars at their custom inputs.
def calc_stats(age, name, endurance, strength, char_class):
	# hitpoints = 0
	# damage = 0

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
	# print(hitpoints, damage, level, strength, endurance, attribute_points, gold)

	class player_character:
		def __init__(self, name, age, char_class, endurance, strength, hitpoints, damage, armor, level, 
			         attribute_points, current_experience, next_level_exp, gold, inventory,
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

		def details(self):
			print("CHARACTER SHEET: \nName: " + str(self.name) + ". \nAge: " + str(self.age) +
				  ". \nClass: " + str(self.char_class).upper() + ". \nEndurance: " + str(self.endurance) +
				  ". \nStrength: " + str(self.strength) + ". \nHitpoints: " + str(self.hitpoints) +
				  ". \nDamage: " + str(self.damage) + ". \nArmor: " + str(self.armor) + ". \nLevel: " + str(self.level) +
				  ". \nAttribute Points: " + str(self.attribute_points) + ". \nCurrent Experience: " +
				  str(self.current_experience) + ". \nExp to next Level: " + 
				  str(self.next_level_exp) + ". \nGold: " + str(self.gold) + ". \nCurrent Weapon: " + str(self.current_weapon) + 
				  ". \nCurrnet Armor: " + str(self.current_armor) + ". ")
	# How else to allow the class object global scope?
	global player
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
	print("\n" * 100)
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
			print("You already have armor. " + "Currnet Armor: " + str(player.current_armor))
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
			print("You aren't wearing any armor.")
		elif player.is_armor_slot_filled == 1:
			player.armor -= self.armor_bonus
			player.is_armor_slot_filled = 0
			player.current_armor = "None"
			player.inventory.append (self.name)

# The player can continuously unequip/equip the item... Need to stop this.
# Build a slot system for items to prevent this.
# Also level requirment must be checked (inform the player if they have insufficient level)
class weapon():
	"""docstring fos weapon"""
	def __init__(self, name, level_requirment, damage_bonus):
		self.name = name
		self.damage_bonus = damage_bonus
		self.level_requirment = level_requirment

	def equip_item(self, player):
		player.damage += self.damage_bonus

	def unequip_item(self, player):
		player.damage += self.damage_bonus

testweapon = weapon("A good stick", 0, 10)
super_test_weapon = weapon("Dragon Slayer", 10, 50)
testarmor = armor("Leather Armor", 0, 10)
super_test_armor = armor("Shavs Wrap", 10, 50)

class enemy():
	def __init__(self, name, hp, dmg, xp):
		self.name = name
		self.hp = hp
		self.dmg = dmg
		# self.lvl = lvl
		# self.reward = reward
		self.xp = xp

wolf = enemy("wolf", 10, 1, 10)





# def character_sheet():
# 	print (" name class stats: inventory:")

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
# 2. Enemies
# 3. Combat.
# 4. 
# 5. Shop.
# 6. items
# 7. character sheet


# credit for this bit of code below https://www.youtube.com/watch?v=hDmnu1qGfkw
# def double_it(formal_parameter):
# 	print(formal_parameter, id(formal_parameter))
# 	doubled = formal_parameter * 2
# 	print(doubled, id(doubled))
# 	return doubled

# argument_value = 3
# print(argument_value, id(argument_value))
# returned_value = double_it(argument_value)
# print(returned_value, id(returned_value))


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