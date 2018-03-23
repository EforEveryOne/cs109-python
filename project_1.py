# start/age/char_class must be definied to avoid errors
	
start = ""
age = ""
char_class = ""
import time

def start_game():
	global start
	global age
	global level
	global total_experience
	global next_level_exp
	global attribute_points
	global strength
	global endurance
	global hitpoints
	global damage
	level = 0
	total_experience = 0
	next_level_exp = 100
	# +2 every level, will be spendable on strength or endurance
	attribute_points = 0
	strength = 0
	endurance = 0

	# takes user input age and determines impacts gameplay and dialogue
	def determine_age():
		global age
		global gold
		global silver
		global copper
		global hitpoints
		global strength
		global endurance
		global char_class

	# currency used to buy things eventually
	# 100 copper = 10 silver = 1 gold
	# determine the characters wealth
		gold = age / 3
		silver = age / 3 * 10
		copper = age / 3 * 100
	# convert FLOAT into an INT so you don't end up with "pieces of coins"
		gold = int(gold)
		silver = int(silver)
		copper = int(copper)
	# crossroads of age choice
		if age <= 0: 
			print (str(age) + "? ")
			time.sleep(2)
			print ("You're not even born yet... Come back when you exist. \nThe End. ")
		# 1-8
		elif age <= 8:
			print (str(age) + "? ")
			time.sleep(2)
			print ("You are too young too young for this adventure. Go take a nap, kid. \nThe End. ")
		# 9-16
		elif age <= 16:
			print (str(age) + "? ")
			time.sleep(2)
			print ("? You are rather young. But you can make it with some luck. ")
			strength = 4
			endurance = 4
			calc_stats()
			choose_class()
		# 17-30
		elif age <= 30:
			print(str(age) + "? ")
			time.sleep(2)
			print("You've got some experience but there's an entire world left to explore.")
			strength = 7
			endurance = 7
			calc_stats()
			choose_class()
		# 31-60
		elif age <= 60:
			print(str(age) + "? ")
			time.sleep(2)
			print("You're not as young as you once were but you've got experience and know your way around the world.")
			strength = 5
			endurance = 5
			calc_stats()
			choose_class()
		# 61-80
		elif age <= 80:
			print(str(age) + "? ")
			time.sleep(2)
			print("Wow. You are at the end of your days... This is probably your last adventure. Lets make it good!")
			strength = 2
			endurance = 2
			calc_stats()
			choose_class()
		# 81+
		elif age >= 81:
			print(str(age) + "? ")
			time.sleep(2)
			print("You are too old! You already had your adventure. Go take a nap. \nThe End. ") 




	# character creation will decide starting stats + inventory
	global name
	while (start) != "yes" or "no":
		start = input("Do you want to go on an adventure? ").lower()
		if "yes" in (start):
			print ("You are about to embark on your very own adventure! ")
			time.sleep(2)
			print ("But first lets get a good look at ya. ")
			time.sleep(2)
			print(" ")
			print ("CHARACTER CREATION: ")
			name = input("So you're an adventurer, eh? What is your name? ")
			print("Hmm...")
			time.sleep(2)
			print (str(name).capitalize() + "? ")
			time.sleep(2)
			print("That's a funny sounding name.")
			time.sleep(3)
			while type(age) != int or type(age) != float:	
				try:
					age = int(input("How old are you? "))
					age = int(age)
					determine_age()
					break
	#ValueError useage found online after much frusteration figuring out how to do this.
	#Found from multiple sites, still took awhile to get it to work/understand it.
				except ValueError:
					print("Be clear with me. Tell me a number! ")
			break
		elif "no" in (start):
			print("If you don't want an adventure it won't be fun anyways. \nThe End. ")
			break
		else:
			print("Be clear with me. Yes or no. Don't complicate things! ")
			time.sleep(1.5)


	# to be placed after wherever exp is gained to check for level up
	if total_experience >= next_level_exp:
		level_up()


def level_up():
# need to modify the existing variables so declare global
	global level
	global total_experience
	global next_level_exp
	global attribute_points
# level up process, level increase, attribute points to spend, set exp for next level
	level += 1
	attribute_points += 2
	total_experience = 0
	next_level_exp = 100 + total_experience * 2
	
	#combat stats, modified by character stats and items
def calc_stats():
	global hitpoints
	global endurance
	global strength
	global damage
	global level
	hitpoints = endurance * 2 + level
	import random
	damage = strength / 2 + level
	damage = int(damage)
	
def choose_class():
	global char_class
	global endurance
	global strength
	global name
	global age
	time.sleep(4)
	print("Tell me...")
	time.sleep(3)
	while (char_class) != "tank" or "aggressive":
		char_class = input("Do you consider yourself more of a Tank or an Aggressive person? ").lower()
		if "tank" in (char_class):
			endurance += 5
			time.sleep(2)
			print ("Congratulations. Your character is complete.")
			time.sleep(1)
			print("Your name is: " + str(name).capitalize() + "\nYour age is: " + str(age) + "\nYour class is: " + str(char_class).capitalize())
			break
		elif "aggressive" in (char_class):
			strength += 5
			time.sleep(2)
			print ("Congratulations. Your character is complete.")
			time.sleep(1)
			print("Your name is: " + str(name).capitalize() + "\nYour age is: " + str(age) + "\nYour class is: " + str(char_class).capitalize())
			break
		else:
			print("Be clear with me. Tank or an Aggressive? ")
			time.sleep(1)



def character_sheet():
	print (" name class stats: inventory:")



# inventory[]
# equipment[]
			# want to have an inventory that can be called that lists every item you have in your inventory.
			# list for equipment, too?



			# currency exchange
			# 1 gold 10 silver 100 copper
			# take in user input pick the currency type you want to buy,
			# user input how much of which currency are you giving them?
			# is it valid?