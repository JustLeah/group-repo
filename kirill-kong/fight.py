from player import *
from mobs import *

fight_str = """
		        _______  __    _______  __    __  ___________
		       |   ____||  |  /  _____||  |  |  | |         |
		       |  |__   |  | |  |  __  |  |__|  | `--|  |---`
		       |   __|  |  | |  | |_ | |   __   |    |  |     
		       |  |     |  | |  |__| | |  |  |  |    |  |     
		       |__|     |__|  \______| |__|  |__|    |__|     
		                                                 
		"""
template = """
You.................................................................................................
"""
def fight():
    while True:
        print(fight_str)
        print(template)
        fight_attack()

def fight_attack():
	command = input("To attack please enter a number between 1-10")

def fight_defend():
	command = input("To defend please enter a number between 1-10")

def print_player_bar():
	print("Blah")

def print_player_name():
	print("You")

def print_mob_bar():
	print("Blah")

def print_mob_name():
	print("Blah")
