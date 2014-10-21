from items import *
from map import rooms
inventory = []
equipped = {
	"head": "none", 
	"chest": "none", 
	"shield": "none", 
	"weapon": "none"
}

stats = {
	"health": 10,
	"attack": 1,
	"defense": 1
}

#Start game at the reception
current_room = rooms["Dark Cabin"]
