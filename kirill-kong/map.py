from items import *
from mobs import *

room_dark_cabin = {
    "name": "Dark Cabin",

    "description":
    """An old and run down cabin, it looks like somewhere that King Kirill would 
send his slaves.""",

    "exits": {"south": "Damp Tunnel", "east": "Open Fields"},
    "chest": [],
    "items": [item_rusty_sword],
    "mobs" : [mob_one, mob_two, mob_three],
    "spawned": []

}

room_open_fields = {
    "name": "Open Fields",

    "description":
    """These fields spread as far as the eye can see. It's a shame
that it's due to being short sighted and a lack of glasses""",

    "exits": {"south": "Dark Forest", "west": "Dark Cabin"},
    "chest": [],
    "items": [item_wooden_shield],
    "mobs" : [mob_one, mob_two, mob_three],
    "spawned": []

}

room_damp_tunnel = {
    "name": "Damp Tunnel",

    "description":
    """This tunnel smells disguisting, nearly as bad as a lecture hall
filled with sweaty computer science students""",

    "exits": {"north": "Dark Cabin", "east": "Dark Forest"},
    "chest": [],
    "items": [],
    "mobs" : [mob_one, mob_two, mob_three],
    "spawned": []
}

room_dark_forest = {
    "name": "Dark Forest",

    "description":
    """This forest is dark, dark enough to not have to worry about 
    hiding someones body. Ever.""",

    "exits": {"north": "Open Fields", "west": "Damp Tunnel", "south": "Dusty Path"},
    "chest": [],
    "items": [],
    "mobs" : [mob_one, mob_two, mob_three],
    "spawned": []
}

room_dusty_path = {
    "name": "Dusty Path",

    "description":
    """This is a dusty path, there is nothing much here, but leads to many more places.""",

    "exits": {"west": "Dim Track", "east": "Illuminated Road", "north": "Dark Forest"},
    "chest": [],
    "items": [],
    "mobs" : [mob_five, mob_nine, mob_ten],
    "spawned": []
}
room_dim_track = {
    "name": "Dim Track",

    "description":
    """You cannot see very well, but to the east there is a small structure.""",

    "exits": {"south": "Old Shack","east": "Dusty Path"},
    "chest": [],
    "items": [],
    "mobs" : [mob_five, mob_nine, mob_ten],
    "spawned": []
}
room_old_shack = {
    "name": "Old Shack",

    "description":
    """You've entered a damp shack, you can hardly see anything but you might find something useful.""",

    "exits": {"north": "Dim Track"},
    "chest": [],
    "items": [],
    "mobs" : [mob_five, mob_nine, mob_ten],
    "spawned": []
}
room_illuminated_road= {
    "name": "Illuminated Road",

    "description":
    """This road is much better than the last two, you can see much clearer and it leads to many places.""",

    "exits": {"west": "Dusty Path", "east": "Damp Cave", "north": "Scary Path", "South": "Abandoned House"},
    "chest": [],
    "items": [],
    "mobs" : [mob_four, mob_thirteen, mob_fourteen],
    "spawned": []
}
room_abandoned_house= {
    "name": "Abandoned House",

    "description":
    """You are in an abandoned house, all the doors are locked, but there is a stair case leading upstairs.""",

    "exits": {"upstairs": "Upstairs", "North": "Illuminated Road"},
    "chest": [],
    "items": [],
    "mobs": [mob_twelve, mob_eleven],
    "spawned": []
}
room_upstairs= {
    "name": "Upstairs",

    "description":
    """You are in an hallway, and again the doors are locked.""",

    "exits": {"down": "Abandoned House"},
    "chest": [],
    "items": [],
    "mobs" : [mob_twelve, mob_eleven],
    "spawned": []
}
room_scary_path= {
    "name": "Scary Path",

    "description":
    """At this point, you are very frightend. The way forward doesn't look to good either.""",

    "exits": {"south": "Illuminated Road", "east": "Haunted Forest"},
    "chest": [],
    "items": [],
    "mobs" : [mob_four, mob_thirteen, mob_fourteen],
    "spawned": []
}
room_haunted_forest= {
    "name": "Haunted Forest",

    "description":
    """You are in a creepy forest, there are many diffrent noises, some don't sound from this world.""",

    "exits": {"south": "Damp Cave","west": "Scary Path"},
    "chest": [],
    "items": [],
    "mobs" : [mob_four, mob_thirteen, mob_fourteen],
    "spawned": []
}
room_damp_cave= {
    "name": "Damp Cave",

    "description":
    """You're in a cave, the air is cold and wet. There are also squeaking sounds, they are probably the bats on the roof.""",

    "exits": {"south": "Castle Grounds", "west": "Illuminated Road", "north": "Haunted Forest"},
    "chest": [],
    "items": [],
    "mobs" : [mob_four, mob_thirteen, mob_fourteen],
    "spawned": []
}
room_castle_grounds= {
    "name": "Castle Grounds",

    "description":
    """You are in the grounds of Kirill Kong's castle, make sure you've got wepons! You never know what could be round the corner!""",

    "exits": {"north": "Damp Cave", "south": "Castle Tower"},
    "chest": [],
    "items": [],
    "mobs" : [mob_seven, mob_eight],
    "spawned": []
}
room_castle_tower= {
    "name": "Castle Tower",

    "description":
    """You're in a vary tall tower, with stairs leading to a chamber.""",

    "exits": {"north": "Castle Grounds", "upstairs": "The Chamber"},
    "chest": [],
    "items": [],
    "mobs" : [mob_seven, mob_eight],
    "spawned": []
}
room_the_chamber= {
    "name": "The Chamber",

    "description":
    """You're in a very large chamber with very large gorilla. IT'S KIRILL KONG! Kill him and save Princess Matt""",

    "exits": {"downstairs": "Castle Tower"},
    "chest": [],
    "items": [],
    "mobs" : [mob_fifteen],
    "spawned": []
}

rooms = {
    "Dark Cabin": room_dark_cabin,
    "Open Fields": room_open_fields,
    "Damp Tunnel": room_damp_tunnel,
    "Dark Forest": room_dark_forest,
    "Dusty Path": room_dusty_path,
    "Dim Track": room_dim_track,
    "Old Shack": room_old_shack,
    "Illuminated Road": room_illuminated_road,
    "Abandoned House": room_abandoned_house,
    "Upstairs": room_upstairs,
    "Scary Path": room_scary_path,
    "Haunted Forest": room_haunted_forest,
    "Damp Cave": room_damp_cave,
    "Castle Grounds": room_castle_grounds,
    "Castle Tower": room_castle_tower,
    "The Chamber": room_the_chamber,
}