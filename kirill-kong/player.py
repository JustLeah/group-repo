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
 	"stats": [15, 1, 1], 
 	"description": "RAWWRRRRRRRRR!", 
 	"loot": [] 
 }

#Start game at the reception
current_room = rooms["Dark Cabin"]
