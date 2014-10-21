#Item stats are in this order HEALTH, ATTACK, DEFENSE
item_rusty_sword = {
    "id": "rusty sword",
    "name": "a Rusty Sword",
    "equipable" : True,
    "stats": [0, 2, 0],  
    "slot" : "weapon",
    "description":
    """This rusty sword would struggle to cut through cheese, even warm cheese. 
It gives me +2 ATTACK!"""
}

item_copper_sword = {
    "id": "copper sword",
    "name": "a Copper sword",
    "equipable" : True,
    "stats": [0, 4, 0],  
    "slot" : "weapon",
    "description":
    """This copper sword gives me +4 ATTACK!"""
}

item_iron_sword = {
    "id": "iron sword",
    "name": "an iron sword",
    "equipable" : True,
    "stats": [0, 6, 0],  
    "slot" : "weapon",
    "description":
    """This iron sword gives me +6 ATTACK!"""
}

item_steel_sword = {
    "id": "steel sword",
    "name": "a steel sword",
    "equipable" : True,
    "stats": [0, 8, 0],  
    "slot" : "weapon",
    "description":
    """This a steel sword gives me +8 ATTACK!"""
}

item_platinum_sword = {
    "id": "platinum sword",
    "name": "a platinum sword",
    "equipable" : True,
    "stats": [0, 10, 0],  
    "slot" : "weapon",
    "description":
    """This platinum sword gives me +10 ATTACK!"""
}

item_wooden_shield = {
    "id": "wooden shield",
    "name": "Wooden Shield",
    "equipable" : True,
    "stats": [0, 0, 2],  
    "slot" : "shield",
    "description":
    """This shield looks like it has been carved by a toddler with ADHD.
It gives me + 2 DEFENSE!"""
}

item_leather_shield = {
    "id": "leather shield",
    "name": "leather Shield",
    "equipable" : True,
    "stats": [0, 0, 1],  
    "slot" : "shield",
    "description":
    """This leather shield gives me + 1 DEFENSE!"""
}

item_iron_shield = {
    "id": "iron shield",
    "name": "iron Shield",
    "equipable" : True,
    "stats": [0, 0, 4],  
    "slot" : "shield",
    "description":
    """This iron shield gives me + 4 DEFENSE!"""
}

item_copper_shield = {
    "id": "copper shield",
    "name": "copper Shield",
    "equipable" : True,
    "stats": [0, 0, 3],  
    "slot" : "shield",
    "description":
    """This copper shield gives me + 3 DEFENSE!"""
}

item_platinum_shield = {
    "id": "platinum shield",
    "name": "platinum Shield",
    "equipable" : True,
    "stats": [0, 0, 5],  
    "slot" : "shield",
    "description":
    """This platinum gives me + 5 DEFENSE!"""
}

item_leather_helmet = {
    "id": "leather helmet",
    "name": "a leather helmet",
    "equipable" : True,
    "stats": [0, 0, 1],  
    "slot" : "head",
    "description":
    """This leather helmet gives me +1 DEFENSE!"""
}

item_copper_helmet = {
    "id": "copper helmet",
    "name": "a copper helmet",
    "equipable" : True,
    "stats": [0, 0, 2],  
    "slot" : "head",
    "description":
    """This copper helmet gives me +2 DEFENSE!"""
}

item_iron_helmet = {
    "id": "iron helmet",
    "name": "an iron helmet",
    "equipable" : True,
    "stats": [0, 0, 3],  
    "slot" : "head",
    "description":
    """This iron helmet gives me +3 DEFENSE!"""
}

item_steel_helmet = {
    "id": "steel helmet",
    "name": "a steel helmet",
    "equipable" : True,
    "stats": [0, 0, 4],  
    "slot" : "head",
    "description":
    """This steel helmet gives me +4 DEFENSE!"""
}

item_platinum_helmet = {
    "id": "platinum helmet",
    "name": "a platinum helmet",
    "equipable" : True,
    "stats": [0, 0, 5],  
    "slot" : "head",
    "description":
    """This platinum helmet gives me +5 DEFENSE!"""
}

item_leather_chestplate = {
    "id": "leather chestplate",
    "name": "a leather chestplate",
    "equipable" : True,
    "stats": [2, 0, 1],  
    "slot" : "chest",
    "description":
    """This leather chestplate gives me +2 HEALTH and +1 DEFENSE!"""
}

item_copper_chestplate = {
    "id": "copper chestplate",
    "name": "a copper chestplate",
    "equipable" : True,
    "stats": [4, 0, 2],  
    "slot" : "chest",
    "description":
    """This copper chestplate gives me +4 HEALTH and +2 DEFENSE!"""
}

item_iron_chestplate = {
    "id": "iron chestplate",
    "name": "an iron chestplate",
    "equipable" : True,
    "stats": [6, 0, 3],  
    "slot" : "chest",
    "description":
    """This iron chestplate gives me +6 HEALTH and +3 DEFENSE!"""
}

item_steel_chestplate = {
    "id": "steel chestplate",
    "name": "a steel chestplate",
    "equipable" : True,
    "stats": [8, 0, 4],  
    "slot" : "chest",
    "description":
    """This steel chestplate gives me +8 HEALTH and +4 DEFENSE!"""
}

item_platinum_chestplate = {
    "id": "platinum chestplate",
    "name": "a platinum chestplate",
    "equipable" : True,
    "stats": [10, 0, 5],  
    "slot" : "chest",
    "description":
    """This platinum chestplate gives me +10 HEALTH and +5 DEFENSE!"""
}



#Adding a dictionary for all the items 
all_items = {
    "rusty sword": item_rusty_sword,
    "copper sword": item_copper_sword,
    "iron sword": item_iron_sword,
    "steel sword": item_steel_sword,
    "platinum sword": item_platinum_sword,
    "wooden shield": item_wooden_shield,
    "copper shield": item_copper_shield,
    "leather shield": item_leather_shield,
    "iron shield": item_iron_shield,
    "platinum shield": item_platinum_shield,
    "leather helmet": item_leather_helmet,
    "copper helmet": item_copper_helmet,
    "iron helmet" : item_iron_helmet,
    "steel helmet": item_steel_helmet,
    "platinum helmet": item_platinum_helmet,
    "leather chestplate": item_leather_chestplate,
    "copper chestplate": item_copper_chestplate,
    "iron chestplate": item_iron_chestplate,
    "steel chestplate": item_steel_chestplate,
    "platinum chestplate": item_platinum_chestplate

}

all_items2 = [
     item_rusty_sword,
     item_copper_sword,
     item_iron_sword,
     item_steel_sword,
     item_platinum_sword,
     item_wooden_shield,
     item_copper_shield,
     item_leather_shield,
     item_iron_shield,
     item_platinum_shield,
     item_leather_helmet,
     item_copper_helmet,
     item_iron_helmet,
     item_steel_helmet,
     item_platinum_helmet,
     item_leather_chestplate,
     item_copper_chestplate,
     item_iron_chestplate,
     item_steel_chestplate,
     item_platinum_chestplate
]
