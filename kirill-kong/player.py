from items import *
from map import rooms
inventory = []
equipped = {
	"head": "none", 
	"chest": "none", 
	"shield": "none", 
	"weapon": "none"
}

player = { 
 	"id": "player", 
 	"name": "You", 
 	"stats": [20, 3, 3], 
 	"description": "RAWWRRRRRRRRR!", 
 	"loot": [] 
 }

#Start game at the Dark Cabin
current_room = rooms["Dark Cabin"]
#Used to test that Kirill Kong was spawning properly!
#current_room = rooms["Castle Tower"]