import time
from random import randint
from utility import clear


global active_game
active_game = 1

while active_game == 1:
	# print(active_game)
	def bad_end():
		"""This is what stops the game when the player dies :("""
		global active_game
		print("You are dead. Game over. ")
		active_game = 0

# Current system for handling items is not fully implemented due to
# my limitation of not yet understanding how to create dynamic items.
# Pre-made items work.
# Creating object group for armor
	class armor():
		"""This is the current implementation of armor.
		   It is fully functional for premade items."""
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
				player.inventory.remove(self.name)
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
				player.inventory.append(self.name)

	# Creating object group for weapons
	class weapon_class():
		"""This is the current implementation of weapons. It is fully functional for premade items."""
		def __init__(self, name, level_requirment, damage_bonus):
			self.name = name
			self.damage_bonus = damage_bonus
			self.level_requirment = level_requirment

		def equip_item(self, player):
			"""This is what handles currently held weapon."""
			if player.level < self.level_requirment:
				print("Your level is too low. \nYour level: " + str(player.level) +
					  ". \n" + "Item level: " + str(self.level_requirment) + ". ")
			elif player.is_weapon_slot_filled == 1:
				print("You already have a weapon. " + "Current Weapon: " + str(player.current_weapon))
			elif (self) in player.inventory:
				player.inventory.remove(self.name)
				# player.inventory = player.inventory - [(self.name)]
				# player.inventory = player.inventory - {(self.name)}
				player.damage += self.damage_bonus
				player.is_weapon_slot_filled = 1
				player.current_weapon = str(self.name)
			# When putting weapon on for the first time (can't remove it from inventory).
			# Can fix by adding the item to inventory when found, that can happen when more features are added.
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
				player.inventory.append(self.name)
				# player.inventory = player.inventory + {(self.name)}

		def weapon_details(self):
			"""Lists off the attributes of the weapon object."""
			print("Weapon details: " + "\nName: " + str(self.name) + ". \nLevel Required: " +
				  str(self.level_requirment) + ". \nDamage: " + str(self.damage_bonus) + ". \n")

# These weapons not fully implemented. Still in testing.
	# need to add a create armor and weapon function that can be dropped as loot. How to randomize the name?
	# chance of a weapon was rolled after defeating an enemy already, if it succeeded, this is called
	def roll_weapon_reward():
		roll = randint(0, 100)
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
		weapon = weapon_class("Weak Sword", 1, randint(1, 4))
		# player.inventory.append (weapon)
		# player.inventory = player.inventory + [(weapon.name)]
		player.inventory = [(weapon)]

	def average_sword():
		global weapon
		weapon = weapon_class("Average Sword", randint(1, 4), randint(4, 10))
		print(weapon)
		# player.inventory.append (weapon)
		player.inventory.append(weapon.name)
		player.details()
		weapon.weapon_details()
		weapon.equip_item(player)
		player.details()

	def super_sword():
		global weapon
		weapon = weapon_class("Super Sword", randint(10, 15), randint(10, 20))

	def best_sword():
		global weapon
		weapon = weapon_class("Best Sword", randint(20, 30), randint(100, 200))

	# testweapon = weapon("A good stick", 0, 10)
	# super_test_weapon = weapon("Dragon Slayer", 10, 50)

	# testarmor = armor("Leather Armor", 0, 10)
	# super_test_armor = armor("Shavs Wrap", 10, 50)

	class enemy_class():
		"""This is the enemy class, it makes objects that have attributes that allow for combat calculations.
		   It gives the enemy life."""
		def __init__(self, name, hitpoints, damage, armor, experience_reward, gold):
			self.name = name
			self.hitpoints = hitpoints
			self.damage = damage
			self.armor = armor
			self.experience_reward = experience_reward
			self.gold = gold

	# creates enemy_class object that is used during all encounters.
	def spawn_wolf():
		global enemy
		# Upped gold for wolf for testing purposes. W/o items+shop implemented you can't sell yet.
		enemy = enemy_class("Wolf", randint(5, 12), randint(1, 3), randint(0, 1), randint(10, 30), randint(4, 10))
	def spawn_bandit():
		global enemy
		enemy = enemy_class("Bandit", randint(10, 20), randint(4, 10), randint(0, 3), randint(50, 100), randint(4, 20))
	def spawn_troll():
		global enemy
		enemy = enemy_class("Troll", randint(20, 50), randint(5, 15), randint(2, 10), randint(500, 1000), randint(20, 50))
	def spawn_dragon():
		global enemy
		enemy = enemy_class("Dragon", randint(1000, 2000), randint(50, 100), randint(20, 50), randint(10000, 30000), randint(1000, 3000))

	# need to add level up print text and time.sleep for the player to see it before moving back
	# to the game and their choice input
	def level_up_check(player):
		"""This makes the player stronger by giving them points to spend."""
		# fill up with print statments, figure out what's wrong.
		if player.current_experience >= player.next_level_exp:
			cross_over_experience = player.current_experience - player.next_level_exp
			player.level += 1
			player.attribute_points += 2
			# total_experience += current_experience
			player.next_level_exp = float(player.next_level_exp)
			player.next_level_exp += player.current_experience ** 1.1
			player.next_level_exp = int(player.next_level_exp)
			player.current_experience += cross_over_experience
			print(str(player.name) + " has leveled up! ")
			print(str(player.name) + "'s current experience: " + str(player.current_experience) + ". ")
			print("Next level at: " + str(player.next_level_exp) + ". ")
			# calling the function because it's supposed to loop through itself, leveling the player up
			# as long as they have an overflow of xp required for the next level.
			# need to fix up the logic.
			level_up_check(player)
		else:
			pass

	def spend_attributes(from_location):
		"""This is what allows the player to increase their Strength and Endurance based on how
		   many spare points they have to spend. both those stats help the player become stronger."""
		print("\nUnspent points: " + str(player.attribute_points) + ". \nCurrent: Strength: "
			  + str(player.strength) + ". \nCurrent Endurance: " + str(player.endurance) + ". \n")
		action = ""
		spend = ""
		print("Available Commands: \nSTRENGTH - increase strength \nENDURANCE - increase endurance \nCANCEL - go back ")
		while action != "strength" or "endurance" or "cancel":
			action = input(str(player.name) + ": ").lower()
			if "strength" in action:
				while type(spend) != int:
					spend = int(input("How many points do you wish to spend? "))
					if spend > player.attribute_points:
						print("You don't have that many attribute points! ")
						break
					elif spend <= player.attribute_points:
						player.strength += spend
						player.attribute_points -= spend
						print("\nUnspent points: " + str(player.attribute_points) + ". \nCurrent: Strength: "
						+ str(player.strength) + ". ")
						player.damage = player.strength / 2 + player.level
						# will need to check for weapon bonus damage and such eventually.
						player.damage = int(player.damage)
						if "from wilderness" in from_location:
							wilderness()
							break
						elif "from town" in from_location:
							town()
						break
					else:
						print("Invalid input. ")
			elif "endurance" in action:
				while type(spend) != int:
					spend = int(input("How many points do you wish to spend? "))
					if spend > player.attribute_points:
						print("You don't have that many attribute points! ")
						spend_attributes(from_location)
					elif spend <= player.attribute_points:
						player.endurance += spend
						player.attribute_points -= spend
						print("\nUnspent points: " + str(player.attribute_points) + ". \nCurrent: Endurance: "
						+ str(player.endurance) + ". ")
						player.max_hitpoints = player.endurance * 2 + player.level
						if "from wilderness" in from_location:
							wilderness()
						elif "from town" in from_location:
							town()
						break
					else:
						print("Invalid input. ")
			elif "cancel" in action:
				print("Not spending any points and going back. ")
				if "from wilderness" in from_location:
					wilderness()
					break
				elif "from town" in from_location:
					town()
					break
			else:
				print("Invalid input. - in spend attribute_points function ")
				action = ""
				spend = ""

	def church():
		"""The Church function is the only mechanic implemented where the player can recover lost hitpoints
		   but they have to pay gold."""
		action = ""
		heal_cost = player.level + 10
		print("=================================")
		print("You entered the church and are greeted by a priest. ")
		time.sleep(1)
		print("Priest: 'Do you want to be healed?' ")
		time.sleep(1)
		print("Priest: 'It only costs " + str(heal_cost) + " gold for you.' ")
		time.sleep(1)
		print("Current gold: " + str(player.gold) + ". ")
		while action != "yes" or "no":
			action = input(str(player.name) + ": ").lower()
			clear(1)
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
						print("=================================")
						clear(2)
						town()
					elif player.gold < heal_cost:
						clear(1)
						print("You don't have enough gold. But Please come back when you do. ")
						print("You leave the church. ")
						print("=================================")
						clear(2)
						town()
			elif "no" in action:
				print("Priest: 'Maybe next time...' \nYou leave the church. ")
				print("=================================")
				clear(2)
				town()
			else:
				print("Priest: 'Sorry, I'm hard of hearing. Did you say yes or no? ")

	def town():
		"""The Town function is the main hub of operations. This is where the player can find the
		   church and eventually manage their inventory and sell items."""
		action = ""
		print("=================================")
		print("You enter the town center. ")
		clear(1)
		print("Available Commands: \nSHOP - buy and sell items. \nCHURCH - recover hitpoints " +
			  "\nWILDERNESS - fight enemies \nPLAYER - inventory, equipment management, skill points ")
		while (action) != "shop" or "church" or "wilderness" or "player":
			action = input(str(player.name).capitalize() + ": ").lower()
			if "shop" in action:
				print("Travelling to the shop... ")
				print("=================================")
				clear(2)
				shop()
				break
			elif "church" in action:
				print("Travelling to the church... ")
				print("=================================")
				clear(2)
				church()
				break
			elif "wilderness" in action:
				print("Travelling to the wilderness... ")
				print("=================================")
				clear(4)
				wilderness()
				break
			elif "player" in action:
				player.details()
				# print(str(player.inventory))
				print("Available Commands: \nEQUIP - doesn't work yet. \nUNEQUIP - doesn't work yet." +
					  " \nATTRIBUTE - spend points to increase stats. \nCANCEL - go back \n")
				while player != "equip" or "unequip" or "attribute" or "cancel":
					sub_action = input(str(player.name) + ": ").lower()
					clear(1)
					if "equip" in sub_action:
						player.details()
						# equip_an_item()
						print("this doesn't work yet")
						print("=================================")
						town()
						break
					elif "unequip" in sub_action:
						player.details()
						# unequip_an_item()
						print("this doesn't work yet")
						print("=================================")
						town()
						break
					elif "attribute" in sub_action:
						print("=================================")
						from_location = "from town"
						print("going to attrbute spend scene from town")
						print("from_location is set to: " + str(from_location))
						spend_attributes(from_location)
						break
					elif "cancel" in sub_action:
						print("Canceled. \n=================================")
						town()
						break
					else:
						print("Invalid command. ")
			else:
				print("Invalid command. ")

	#  Eventually a set of commands that allows the player to swap out equipment, spend skillpoints, and use items.
	# def player_command():
		"""This is where the player will be able to check their character details, spend their attribute points,
		   and manage inventory and equipment."""
		# print("placeholder ")

	def town_first_visit():
		"""This will be used for a relevant storyline in future versions of the game, also will
		   serve as a tutorial for the player to learn about each command they have access to. """
		print("first town visit, introduction ")
		# print("now sending the player to the normal town. You can visit the Shop, the Church, the Wilderness, or check your supplies. ")
		# Have the player test combat by getting into a fight with a drunk person, the player
		# has no weapons yet so they won't kill them.
		# The townspeople congratulate the player
		# introduce the player to the church that heals them.
		# introduce the player to the shop
		# shop will tell them about the wilderness
		# player leaves the shop and goes to the "main square"
		# this is where the player takes control.
		# They can examine their player details, that means, stats, inventory,
		# They can head to the church, shop, or wilderness.
		town()

	def wilderness():
		"""The wilderness is where the player is able to get into fights and earn rewards."""
		action = ""
		print("=================================")
		print("You are in the wilderness! ")
		print("You can use the following commands: \n\nEXPLORE - fight enemies \nTOWN - leave wilderness " +
			  "\nPLAYER - inventory, equipment management, skill points ")
		while action != "explore" or "town" or "player":
			action = input(str(player.name).capitalize() + ": ").lower()
			clear(1)
			if "explore" in action:
				print("You wander around the wilderness... ")
				print("=================================")
				clear(4)
				encounter(player)
				break
			elif "town" in action:
				print("Travelling back to town... ")
				print("=================================")
				clear(4)
				town()
				break
			elif "player" in action:
				player.details()
				# print(str(player.inventory))
				print("Available Commands: \nEQUIP - doesn't work yet. \nUNEQUIP - doesn't work yet." +
					  " \nATTRIBUTE - spend points to increase stats. \nCANCEL - go back \n")
				while player != "equip" or "unequip" or "attribute" or "cancel":
					sub_action = input(str(player.name) + ": ").lower()
					clear(1)
					if "equip" in sub_action:
						player.details()
						# equip_an_item()
						print("this doesn't work yet")
						print("=================================")
						clear(1)
						wilderness()
						break
					elif "unequip" in sub_action:
						player.details()
						# unequip_an_item()
						print("this doesn't work yet")
						print("=================================")
						clear(1)
						wilderness()
						break
					elif "attribute" in sub_action:
						print("=================================")
						from_location = "from wilderness"
						print("going to attribute spend scene from wilderness")
						print("from_location is set to: " + str(from_location))
						spend_attributes(from_location)
					elif "cancel" in sub_action:
						print("Canceled. \n=================================")
						clear(1)
						wilderness()
						break
					else:
						print("Invalid command. ")
			else:
				print("Invalid Command. ")

	# Can simplify this be breaking down into functions...
	def players_turn(player, enemy, run_away):
		"""This is where combat happens. The player takes an action and based on the results,
		   they win, die, or the enemy takes a turn."""
		print("================================= \n" + (player.name).capitalize() +
			  "'s TURN: \nYou can use the following commands: \nATTACK - deal damage \nRUN - attempt to run \nITEM - not implemented yet\n ")
		if run_away == 0:
			if player.current_hitpoints <= 0:
				bad_end()
			# elif enemy.hitpoints <= 0:
				# clear(2)
			elif enemy.hitpoints >= 1:
				action = ""
				while action != "attack" or "run" or "item":
					action = input(str(player.name).capitalize() + ": ").lower()
					clear(1)
					if "attack" in (action):
						combat_damage = player.damage
						combat_damage -= enemy.armor
						if combat_damage > 0:
							enemy.hitpoints -= combat_damage
							clear(1)
							print("You struck the enemy for " + str(combat_damage) + " damage after " + str(enemy.armor) +
								  " was blocked by their armor! ")
							if enemy.hitpoints >= 1:
								print("================================= \n")
								time.sleep(3)
								enemy_turn(player, enemy, run_away)
								break
							# check if enemy is dead
							elif enemy.hitpoints <= 0:
								clear(2)
								print("You defeated the " + str(enemy.name) + "! ")
								if enemy.gold > 0:
									print("You found: " + str(enemy.gold) + " gold! ")
									player.gold += enemy.gold
									print("You now have a total of: " + str(player.gold) + " gold! ")
									player.current_experience += enemy.experience_reward
									print("You earned: " + str(enemy.experience_reward) + " experience! ")
									print("You now have a total of: " + str(player.current_experience) + " experience! ")
									level_up_check(player)
									break
								else:
									player.current_experience += enemy.experience_reward
									print("You earned: " + str(enemy.experience_reward) + " experience! ")
									print("You now have a total of: " + str(player.current_experience) + " experience! ")
									level_up_check(player)
									break
						else:
							clear(1)
							print("The " + str(enemy.name) + "'s armor is too high! ")
							print("================================= \n")
							enemy_turn(player, enemy, run_away)
							break
					elif "run" in (action):
						clear(1)
						run_chance = randint(1, 100)
						print("You attempt to run away: \nYou rolled: " + str(run_chance) + " out of 100. ")
						if player.age <= 16:
							if run_chance <= 90:
								run_away = 1
								print("You succesfully escaped the " + str(enemy.name) +
									  "! \n================================= \n")
								break
							else:
								run_away = 0
								print("The " + str(enemy.name) + " prevented you from escaping! \n")
								enemy_turn(player, enemy, run_away)
								break
						elif player.age <= 30:
							if run_chance <= 50:
								run_away = 1
								print("You succesfully escaped the " + str(enemy.name) +
									  "! \n================================= \n")
								break
							else:
								run_away = 0
								print("The " + str(enemy.name) + " prevented you from escaping! \n")
								enemy_turn(player, enemy, run_away)
								break
						elif player.age <= 60:
							if run_chance <= 30:
								run_away = 1
								print("You succesfully escaped the " + str(enemy.name) +
									  "! \n================================= \n")
								break
							else:
								run_away = 0
								print("The " + str(enemy.name) + " prevented you from escaping! \n")
								enemy_turn(player, enemy, run_away)
								break
						elif player.age <= 80:
							if run_chance <= 10:
								run_away = 1
								print("You succesfully escaped the " + str(enemy.name) +
									  "! \n================================= \n")
								break
							else:
								run_away = 0
								print("The " + str(enemy.name) + " prevented you from escaping! \n")
								enemy_turn(player, enemy, run_away)
								break
					# Below commented out code is to be reworked.
						# run(player, enemy)
						# break
					# elif "item" in (action):
					# 	# loop through actons with items can take off an item, but need to equip an item.
					# 	print(player.inventory)
					# 	item_action = input("use, item name ")
					# 	# if item_action = How to check for weapon/armor/or other item?
					# 	break
					else:
						print("Please type 'attack' 'run' or 'item' into the console. ")
			else:
				wilderness()

	def enemy_turn(player, enemy, run_away):
		# If run away is not true, continue the fight
		if run_away == 0:
			if player.current_hitpoints <= 0:
				bad_end()
			elif enemy.hitpoints >= 1:
				print("================================= \nENEMY TURN:")
				time.sleep(1)
				combat_damage = enemy.damage
				combat_damage -= player.armor
				if combat_damage > 0:
					player.current_hitpoints -= combat_damage
					print("The " + str(enemy.name) + " hit you for " + str(combat_damage) + " damage after " + str(player.armor) +
						  " was blocked by your armor!")
					time.sleep(1)
					print("Player HP: " + str(player.current_hitpoints) + "/" + str(player.max_hitpoints))
					# check if player is dead
					if player.current_hitpoints <= 0:
						print("================================= \n")
						bad_end()
					else:
						print("================================= \n")
						clear(1)
						players_turn(player, enemy, run_away)
				else:
					print("Your armor protects you from the " + str(enemy.name) + "! ")
					clear(1)
					players_turn(player, enemy, run_away)
			else:
				print("the enemy should be dead!")
		else:
			print("the player should have ran away!")

	def create_random_enemy():
		"""This is how randomized enemies are decided for an encounter in the wilderness."""
		randomize_spawn = randint(1, 100)
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
		global active_game
		"""Encounter is the function that initiates the combat scene between the player and an enemy."""
		# Set run away to 0, which is no.
		run_away = 0
		# Create a randomized enemy.
		create_random_enemy()
		print("\nA " + str(enemy.name) + " has appeared! \n")
		time.sleep(1)
		# Decide who goes first influenced by player age.
		turn_order = randint(1, 100)
		print("Deciding turn order...")
		time.sleep(2)
		print("You rolled: " + str(turn_order) + " out of 100. ")
		clear(1)
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
			time.sleep(1)
			enemy_turn(player, enemy, run_away)
		elif player_first == 1:
			print("You're able to act before the " + str(enemy.name) + " realizes! \n")
			time.sleep(1)
			players_turn(player, enemy, run_away)
		print("The encounter is over! ")
		print("=================================")
		clear(2)
		# break out of the game loop if player is dead.
		if active_game == 1:
			wilderness()

	def shop():
		print("The shop is closed (not created yet)")
		print("Heading back to town.")
		print("=================================")
		clear(2)
		town()
	# rough outline for shop in the town scene
	# if player.gold >= item__shop_price:
		# player.gold -= item__shop_price:
		# player.inventory.append (self.name)

	def calc_stats(age, name, endurance, strength, char_class):
		"""This compiles all the information gathered by earlier functions at the start of the game."""
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
		# inventory = {}
		is_weapon_slot_filled = 0
		is_armor_slot_filled = 0
		current_weapon = "None"
		current_armor = "None"

		# Creates the player_character class object and passes in all the vars at their custom inputs.
		# will need to change player hipoints to a max hitpoints and a current hitpoints.
		class player_character:
			"""This is where the playr character is made."""
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
				# self.inventory = {}
				self.is_weapon_slot_filled = is_weapon_slot_filled
				self.is_armor_slot_filled = is_armor_slot_filled
				self.current_weapon = current_weapon
				self.current_armor = current_armor

			# Character sheet (player information).
			def details(self):
				"""This is a clear description of player information."""
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
				# Will be used to allow for easy player interface when managing equpiment+inventory.
				print("placeholder")

		# Make the player global to give full scope access to the rest of the functions that rely on it.
		global player
		# Create the player with all the required information gathered in the previous functions.
		player = player_character(name, age, char_class, endurance, strength, current_hitpoints, max_hitpoints,
								  damage, armor, level, attribute_points, current_experience, next_level_exp,
								  gold, inventory, is_weapon_slot_filled, is_armor_slot_filled, current_weapon,
								  current_armor)
		player.details()
		time.sleep(5)
		print("\nI wish you well on your adventure, " + (player.name).capitalize() + "!")
		clear(2)
		print(" \n\nYour eyes are getting heavy...")
		clear(2)
		print("Your vision is blurry...")
		clear(2)
		print("The wolrd fades away...")
		clear(4)
		print("You wake up on a dusty road.")
		town_first_visit()

	def input_class(age, name, endurance, strength):
		"""Takes in previous inputs and continues to gather more info about the player to build the character."""
		char_class = ""
		clear(1)
		print("Tell me...")
		clear(1)
		while (char_class) != "defensive" or "aggressive":
			char_class = input("Do you consider yourself more of a Defensive or an Aggressive person? ").lower()
			if "defensive" in (char_class):
				char_class = "Tank"
				endurance += 5
				clear(1)
				print("Congratulations. Your character is complete. \nYou are ready for adventure! \n\n")
				clear(1)
				calc_stats(age, name, endurance, strength, char_class)
				break
			elif "aggressive" in (char_class):
				char_class = "Fighter"
				strength += 5
				clear(1)
				print("Congratulations. Your character is complete. \nYou are ready for adventure! \n\n")
				clear(1)
				calc_stats(age, name, endurance, strength, char_class)
				break
			else:
				print("Be clear with me. Defensive or an Aggressive? ")
				# time.sleep(0.5)

	def input_age(age, name):
		"""This takes in user input and determines what the player's age will be.
		   It impacts gameplay and dialogue."""
		if age <= 0:
			clear(1)
			print(str(age) + "? ")
			clear(1)
			print("You're not even born yet... Come back when you exist. \nThe End. ")
		# 1-8
		elif age <= 8:
			clear(1)
			print(str(age) + "? ")
			clear(1)
			print("You are too young too young for this adventure. Go take a nap, kid. \nThe End. ")
		# 9-16
		elif age <= 16:
			clear(1)
			print(str(age) + "? ")
			clear(1)
			print("? You are rather young. But you can make it with some luck. ")
			strength = 4
			endurance = 4
			input_class(age, name, endurance, strength)
		# 17-30
		elif age <= 30:
			clear(1)
			print(str(age) + "? ")
			clear(1)
			print("You've got some experience but there's an entire world left to explore.")
			strength = 8
			endurance = 8
			input_class(age, name, endurance, strength)
		# 31-60
		elif age <= 60:
			clear(1)
			print(str(age) + "? ")
			clear(1)
			print("You're not as young as you once were but you've got experience and know your way around the world.")
			strength = 6
			endurance = 6
			input_class(age, name, endurance, strength)
		# 61-80
		elif age <= 80:
			clear(1)
			print(str(age) + "? ")
			clear(1)
			print("Wow. You are at the end of your days... This is probably your last adventure. Lets make it good!")
			strength = 2
			endurance = 2
			input_class(age, name, endurance, strength)
		# 81+
		elif age >= 81:
			clear(1)
			print(str(age) + "? ")
			clear(1)
			print("You are too old! You already had your adventure. Go take a nap. \nThe End. ")

	def start():
		"""This is what starts the game."""
		start = ""
		name = ""
		age = ""
		while (start) != "yes" or "no":
			start = input("Do you want to go on an adventure? ").lower()
			if "yes" in (start):
				print("You are about to embark on your very own adventure! ")
				clear(1)
				print("But first lets get a good look at ya. ")
				clear(1)
				print("CHARACTER CREATION: ")
				name = input("So you're an adventurer, eh? What is your name? ")
				clear(1)
				print("Hmm...")
				clear(1)
				print(str(name).capitalize() + "? ")
				clear(1)
				print("That's a funny sounding name.")
				clear(1)
				while type(age) != int or type(age) != float:
					try:
						age = int(input("How old are you? "))
						age = int(age)
						# passing in age and name into the next function because
						# it needs their information
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

	# Jumpstart the game inside the loop
	if active_game == 1:
		start()
