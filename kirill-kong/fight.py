import random
from kirillkong import *
from player import *
from mobs import *
import copy
import os, ctypes

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

def fight(current_mob_id, current_room):
	global current_mob
	global damage_dealt
	global damage_received
	initialhealth = player['stats'][0]
	#Set the mob passed through to the current mob
	if current_mob == "none":
		current_mob = copy.deepcopy(all_mobs[current_mob_id])
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
	

def fight_attack(attacker, defender):
	global damage_dealt
	global turn
	attackroll = input("To attack please enter a number between 1-10: ")
	if attackroll:
		if int(attackroll) < 11 and int(attackroll) > 0:
			if defender['id'] != "player":
				defenceroll = random.randint(1, 10)
			damagedifference = abs(int(attackroll) - int(defenceroll))
			finaldamage = int(damagedifference) + int(attacker['stats'][1]) - int(defender['stats'][2])
			damage_dealt = finaldamage
			defender['stats'][0] = defender['stats'][0] - finaldamage
			turn = "defend"
			return(finaldamage)


def fight_defend(attacker, defender):
	global damage_received
	global turn
	player_defenseroll = input("To defend yourself please enter a number between 1-10: ")
	if player_defenseroll:
		if int(player_defenseroll) < 11 and int(player_defenseroll) > 0:
			if attacker['id'] != "player":
				mob_attackroll = random.randint(1,10)
			damagedifference = abs(int(mob_attackroll) - int(player_defenseroll))
			finaldamage = int(damagedifference) + int(attacker['stats'][1]) - int(defender['stats'][2])
			damage_received = finaldamage
			defender['stats'][0] = defender['stats'][0] - finaldamage
			turn = "attack"
			return(finaldamage)


def print_player_bar(stats):
	current_health = stats[0]
	return "/" * current_health

def print_mob_bar(current_mob):
	current_health = current_mob['stats'][0]
	return "\\" * current_health

def return_player_name():
	return "You"

def return_mob_name(current_mob):
	return current_mob['name']

def join_names(current_mob):
	mob_name = return_mob_name(current_mob)
	player_name = return_player_name()
	length = len(mob_name)
	amountofspaces = 97-length
	spaces = " " * amountofspaces
	print(player_name + spaces + mob_name)

def join_health_bars(current_mob_id):
	phealth = print_player_bar(player['stats'])
	mhealth = print_mob_bar(current_mob_id)
	totallen = 100
	totallen = totallen - len(phealth) - len(mhealth)
	print(phealth + (" " * totallen) + mhealth)