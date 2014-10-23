import random
from kirillkong import *
from player import *
from mobs import *
from newparse import *
import copy
import os, ctypes

#Initilising variblies that will be used later on
turn = "attack"
damage_dealt = ""
damage_received = ""
current_mob = "none"
youattack = """
			    ___  _______________   ________ __
			   /   |/_  __/_  __/   | / ____/ //_/
			  / /| | / /   / / / /| |/ /   / ,<   
			 / ___ |/ /   / / / ___ / /___/ /| |  
			/_/  |_/_/   /_/ /_/  |_\____/_/ |_|  
		                                     
"""
fight_str = """
		        _______  __    _______  __    __  ___________
		       |   ____||  |  /  _____||  |  |  | |         |
		       |  |__   |  | |  |  __  |  |__|  | `--|  |---`
		       |   __|  |  | |  | |_ | |   __   |    |  |     
		       |  |     |  | |  |__| | |  |  |  |    |  |     
		       |__|     |__|  \______| |__|  |__|    |__|     
		                                                 
"""
youdefend = """
			    ____  ___________________   ______ 
			   / __ \/ ____/ ____/ ____/ | / / __ \\
			  / / / / __/ / /_  / __/ /  |/ / / / /
			 / /_/ / /___/ __/ / /___/ /|  / /_/ / 
			/_____/_____/_/   /_____/_/ |_/_____/  
                                       
"""
#This is the main fight loop it calls on the attacking and defending functions
def fight(current_mob_id, current_room):
	global current_mob
	global damage_dealt
	global damage_received
	initialhealth = player['stats'][0]
	#Set the mob passed through to the current mob
	#Make a deep copy so that we can change the mob values without editing the actual mob
	if current_mob == "none":
		current_mob = copy.deepcopy(all_mobs[current_mob_id])
	#Checck that both the player and mob are alive
	while player['stats'][0] > 0 and current_mob['stats'][0] > 0:
		clear = lambda: os.system('cls')
		clear()
		if type(damage_dealt) == int:
			if damage_dealt > 0:
				print(str(damage_dealt) + " damage was dealt")
				damage_dealt = ""
			else:
				print("You dealt 0 damage!")
				damage_dealt = ""
		if type(damage_received) == int:
			if damage_received > 0:
				print("You took %s damage!" % str(damage_received))
				damage_received = ""
			else:
				print("You took 0 damage!")
				damage_received = ""
    	#Print the fight ASCII
		print(fight_str)
		if turn == "attack":
			print(youattack)
		else:
			print(youdefend)
		join_names(current_mob)
		join_health_bars(current_mob)
		print()
		if turn == "attack":
			fight_attack(player, current_mob)
		else:
			fight_defend(current_mob, player)
	#Check which person is dead and either show the game over screen if its a player
	#Or drop the loot if its a mob		
	else:
		clear = lambda: os.system('cls')
		clear()
		if player['stats'][0] <= 0:
			game_over()
			exit()

		if current_mob['id'] == "15" and current_mob['stats'][0] <= 0:
			completion()
			exit()

		print("You have killed a %s!" % current_mob['name'])
		counter = 1
		randcounter = random.randint(1, len(current_mob['loot']))
		for item in current_mob['loot']:
			if randcounter == counter:
				current_room['items'].append(item)
				print("The %s dropped a %s!" % (current_mob['name'], item['name']))
				break
			counter = counter + 1
		player['stats'][0] = initialhealth
		del current_mob
		del damage_dealt
		damage_dealt = ""
		current_mob = "none"
		current_room['spawned'] = []
	
#This function will calculate the damage that has been done and return that value
def fight_attack(attacker, defender):
	global damage_dealt
	global turn
	attackroll = strip_text(input("To attack please enter a number between 1-10: "))
	if attackroll:
		if int(attackroll) < 11 and int(attackroll) > 0:
			if defender['id'] != "player":
				defenceroll = random.randint(1, 10)
			damagedifference = abs(int(attackroll) - int(defenceroll))
			finaldamage = int(damagedifference) + int(attacker['stats'][1]) - int(defender['stats'][2])
			damage_dealt = finaldamage
			if finaldamage > 0:
				defender['stats'][0] = defender['stats'][0] - finaldamage
			turn = "defend"
			return(finaldamage)

#This function will calculate the damage that has been taken and return that value
def fight_defend(attacker, defender):
	global damage_received
	global turn
	player_defenseroll = strip_text(input("To defend yourself please enter a number between 1-10: "))
	if player_defenseroll:
		if int(player_defenseroll) < 11 and int(player_defenseroll) > 0:
			if attacker['id'] != "player":
				mob_attackroll = random.randint(1,10)
			damagedifference = abs(int(mob_attackroll) - int(player_defenseroll))
			finaldamage = int(damagedifference) + int(attacker['stats'][1]) - int(defender['stats'][2])
			damage_received = finaldamage
			if finaldamage > 0:
				defender['stats'][0] = defender['stats'][0] - finaldamage
			turn = "attack"
			return(finaldamage)

#Make a health bar
def print_player_bar(stats):
	current_health = stats[0]
	return "/" * current_health

#Make a health bar
def print_mob_bar(current_mob):
	current_health = current_mob['stats'][0]
	return "\\" * current_health

def return_player_name():
	return "You"

def return_mob_name(current_mob):
	return current_mob['name']

#Join the player and mob names and set a certain amount of spaces so that it takes up the whole screen
def join_names(current_mob):
	mob_name = return_mob_name(current_mob)
	player_name = return_player_name()
	length = len(mob_name)
	amountofspaces = 97-length
	spaces = " " * amountofspaces
	print(player_name + spaces + mob_name)

#Join the player and mob health bars and set a certain amount of spaces so that it takes up the whole screen
def join_health_bars(current_mob_id):
	phealth = print_player_bar(player['stats'])
	mhealth = print_mob_bar(current_mob_id)
	totallen = 100
	totallen = totallen - len(phealth) - len(mhealth)
	print(phealth + (" " * totallen) + mhealth)