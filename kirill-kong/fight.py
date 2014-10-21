import random
from player import *
from mobs import *
import os, ctypes

damage_dealt = ""
current_mob = ""
fight_str = """
		        _______  __    _______  __    __  ___________
		       |   ____||  |  /  _____||  |  |  | |         |
		       |  |__   |  | |  |  __  |  |__|  | `--|  |---`
		       |   __|  |  | |  | |_ | |   __   |    |  |     
		       |  |     |  | |  |__| | |  |  |  |    |  |     
		       |__|     |__|  \______| |__|  |__|    |__|     
		                                                 
"""

def fight(current_mob_id):
    while True:
    	clear = lambda: os.system('cls')
    	clear()
    	if damage_dealt:
    		print(str(damage_dealt) + " damage was dealt")
    	#Set the mob passed through to the current mob
    	current_mob = all_mobs[current_mob_id]
    	#Print the fight ASCII
    	print(fight_str)
    	join_names(current_mob_id)
    	join_health_bars(current_mob_id)
    	print()
    	fight_attack(player, current_mob)

def fight_attack(attacker, defender):
	global damage_dealt
	attackroll = input("To attack please enter a number between 1-10: ")
	if defender['id'] != "player":
		defenceroll = random.randint(1, 10)
	damagedifference = abs(int(attackroll) - int(defenceroll))
	finaldamage = int(damagedifference) + int(attacker['stats'][1]) - int(defender['stats'][2])
	damage_dealt = finaldamage
	defender['stats'][0] = defender['stats'][0] - finaldamage
	return(finaldamage)


def fight_defend(attacker, defender):
	value = input("To defend please enter a number between 1-10")

def print_player_bar(stats):
	current_health = stats[0]
	return "/" * current_health

def print_mob_bar(current_mob_id):
	current_mob = all_mobs[current_mob_id]
	current_health = current_mob['stats'][0]
	return "\\" * current_health

def return_player_name():
	return "You"

def return_mob_name(current_mob_id):
	current_mob = all_mobs[current_mob_id]
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