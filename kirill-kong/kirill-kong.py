#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from newparse import *
import os, ctypes



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:
    """
    item_list = []
    for i in items:
        item_list.append(i['name'])
    final_list = ", ".join(item_list)
    return final_list


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    """
    item_list = list_of_items(room['items'])
    if len(item_list) > 0:
        string = "There is %s here." % item_list
        print(string)
        print("")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.".
    """
    item_list = list_of_items(items)
    if len(item_list) > 0:
        string = "You have %s." % item_list
        print(string)
        print("")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this).
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    if print_room_items(room):
        print()


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:
    """
    print("GO %s to the %s." % (direction.upper(), leads_to))


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print
    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    #Output each item in the room
    for item in room_items:
        name = str(item['id']).upper()
        desc = str(item['name']).lower()
        print("TAKE %s to take %s." % (name, desc))
    if len(inventory) > 0:
        print("DROP followed by item name to drop an item")
        print("INVENTORY to see a list of items that are carrying")
    for i in inventory:
        if i['equipable']:
            print("EQUIP followed by the item name to equip the item")
            break 
    print("EQUIPPED to see what you have equipped")  
    print("EXAMINE followed by an items name to examine it")
    print("STATS to see your current stats")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """ 
    global current_room
    direction = ' '.join(direction)
    if is_valid_exit(current_room['exits'], direction):
        current_room = rooms[current_room['exits'][direction]]
    else:
        print("You cannot go there!")


def execute_take(item_id):
    #Added a dictionary of all items for this function to make checking the items easier
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    #Turn the list to a string if more then one word
    item_id = ' '.join(item_id)
    global current_mass
    #Check to see if the item is in that room
    if item_id in all_items:
        if all_items[item_id] in current_room['items']:
            #remove the item from the room it is in
            current_room['items'].remove(all_items[item_id])
            #add the item to the player inventory
            inventory.append(all_items[item_id]) 
            print("You picked up the %s" % item_id)   
    else:
        print("You cannot take that!")


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    item_id = ' '.join(item_id)
    global current_mass
    #Check to see if the item is in the inventory
    if item_id in all_items:    
        if all_items[item_id] in inventory:
            #remove the item from the inventory
            inventory.remove(all_items[item_id])
            #add the item to the room the player is in
            current_room['items'].append(all_items[item_id])
            print("You dropped the %s" % item_id)
    else:
        print("You do not have that!")


def equip_item(item_id):
    """This function will equip the item and give the player the benifical stats
    as well as moving it from inventory to equiped items
    """  
    #Turn the list to a string if more then one word
    item_id = ' '.join(item_id)
    #Check to see if the item exists
    if item_id in all_items:
        if all_items[item_id] in inventory and all_items[item_id]['equipable'] == True:
            #Check that slot is empty          
            if equipped[all_items[item_id]['slot']] == "none":
                #remove the item from the inventory
                inventory.remove(all_items[item_id])
                #add the item to the player equiped items
                equipped[all_items[item_id]['slot']] = all_items[item_id]
                #add the benificial stats to your stats
                statcounter = 0
                for s in all_items[item_id]['stats']:
                    if statcounter == 0:  
                        stats['health'] = stats['health'] + s
                        statcounter = statcounter + 1
                    elif statcounter == 1:  
                        stats['attack'] = stats['attack'] + s
                        statcounter = statcounter + 1
                    elif statcounter == 2:  
                        stats['defense'] = stats['defense'] + s
                        statcounter = statcounter + 1
                print("%s has been equipped!" % item_id.upper()) 
            else:
                print("Please UNEQUIP the %s first!" % equipped[all_items[item_id]['slot']]['id'].upper())
        else:
            print("You cannot equip this item!")      
    else:
        print("You do not have this item!")


def unequip_item(item_id):
    """This function will unequip the item removing the benifical stats
    as well as moving it from equiped items to the inventory
    """  
    #Turn the list to a string if more then one word
    item_id = ' '.join(item_id)
    #Check to see if the item exists
    if item_id in all_items:
        #Check to see if the item is equipped
        for e in equipped:
            if equipped[all_items[item_id]['slot']] == all_items[item_id]:
                #remove the item from the inventory
                equipped[all_items[item_id]['slot']] = "none"
                #add the item to the player equiped items
                inventory.append(all_items[item_id]) 
                #remove the benificial stats from your stats
                statcounter = 0
                for s in all_items[item_id]['stats']:
                    if statcounter == 0:  
                        stats['health'] = stats['health'] - s
                        statcounter = statcounter + 1
                    elif statcounter == 1:  
                        stats['attack'] = stats['attack'] - s
                        statcounter = statcounter + 1
                    elif statcounter == 2:  
                        stats['defense'] = stats['defense'] - s
                        statcounter = statcounter + 1
                print("%s has been unequipped!" % item_id.upper())
                break   
        else:
            print("You do not have this item equipped!")
    else:
        print("This item doesn't exist!")


def equipped_items():
    """This function will show you all of your equipped items as well
    as any empty slots you have
    """  
    for e in equipped:
        if equipped[e] == "none":
            print("You have no %s equipped." % e)
        else:
            print("You have %s equipped!" % str(equipped[e]['name']))


def show_stats():
    """This function will show you your current stat values
    """  
    for s in stats:
        print("Your current %s is %i." % (s.upper(), stats[s]))


def examine_item(item_name):
    """This function will pull up the description for an item"""
    #Turn the list to a string if more then one word
    item_name = ' '.join(item_name)
    print(all_items[item_name]['description'])


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """
    #Clear the screen first!
    clear = lambda: os.system('cls')
    clear()
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1:])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1:])
        else:
            print("Take what?")

    elif command[0] == "equip":
        if len(command) > 1:
            equip_item(command[1:])
        else:
            print("Equip what?")

    elif command[0] == "unequip":
        if len(command) > 1:
            unequip_item(command[1:])
        else:
            print("Unequip what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1:])
        else:
            if len(inventory) > 0:
                for item in inventory:
                    name = str(item['id']).upper()
                    desc = str(item['name']).lower()
                    print("DROP %s to drop %s" % (name, desc))
            else:
                print("You don't have anything to drop!")

    elif command[0] == "equipped":
        if len(command) == 1:
            equipped_items()

    elif command[0] == "examine":
        if len(command) == 1:
            print("Use EXAMINE followed by item name e.g. EXAMINE RUSTY SWORD")
        else:
            examine_item(command[1:])

    elif command[0] == "stats":
        if len(command) == 1:
            show_stats()

    elif command[0] == "inventory":
        if len(command) == 1:
            print_inventory_items(inventory)

    else:
        print("This makes no sense.")


def menu(exits, room_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """
    # Display menu
    print_menu(exits, room_items, inventory)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        # Display game status (room description)
        print_room(current_room)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"])

        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    #Clear the screen first!
    os.system("mode con cols=100")
    clear = lambda: os.system('cls')
    clear()
    main()