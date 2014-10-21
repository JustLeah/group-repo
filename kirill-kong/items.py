#Item stats are in this order HEALTH, ATTACK, DEFENSE
item_rusty_sword = {
    "id": "rusty sword",
    "name": "a Rusty Sword",
    "equipable" : True,
    "stats": [0, 1, 0],  
    "slot" : "weapon",
    "description":
    """This rusty sword would struggle to cut through cheese, even warm cheese. 
It gives me +1 ATTACK!"""
}

item_rusty_axe = {
    "id": "rusty axe",
    "name": "a Rusty Axe",
    "equipable" : True,
    "stats": [0, 1, 0],  
    "slot" : "weapon",
    "description":
    """This axe is rusty and hits like a wet noodle. 
It gives me +1 ATTACK!"""
}

item_wooden_shield = {
    "id": "wooden shield",
    "name": "Wooden Shield",
    "equipable" : True,
    "stats": [0, 0, 1],  
    "slot" : "shield",
    "description":
    """This shield looks like it has been carved by a toddler with ADHD.
It gives me + 1 DEFENSE!"""
}


#Adding a dictionary for all the items 
all_items = {
    "rusty sword": item_rusty_sword,
    "rusty axe": item_rusty_axe,
    "wooden shield": item_wooden_shield
}
