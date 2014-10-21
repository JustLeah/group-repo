from items import *

room_dark_cabin = {
    "name": "Dark Cabin",

    "description":
    """An old and run down cabin, it looks like somewhere that King Kirill would 
send his slaves.""",

    "exits": {"south": "Damp Tunnel", "east": "Open Fields"},

    "items": [item_rusty_sword, item_rusty_axe]
}

room_open_fields = {
    "name": "Open Fields",

    "description":
    """These fields spread as far as the eye can see. It's a shame
that it's due to being short sighted and a lack of glasses""",

    "exits": {"south": "Dark Forest", "west": "Dark Cabin"},

    "items": [item_wooden_shield]
}

room_damp_tunnel = {
    "name": "Damp Tunnel",

    "description":
    """This tunnel smells disguisting, nearly as bad as a lecture hall
filled with sweaty computer science students""",

    "exits": {"north": "Dark Cabin", "east": "Dark Forest"},

    "items": []
}

room_dark_forest = {
    "name": "Dark Forest",

    "description":
    """This forest is dark, dark enough to not have to worry about 
    hiding someones body. Ever.""",

    "exits": {"north": "Open Fields", "west": "Damp Tunnel"},

    "items": []
}

rooms = {
    "Dark Cabin": room_dark_cabin,
    "Open Fields": room_open_fields,
    "Damp Tunnel": room_damp_tunnel,
    "Dark Forest": room_dark_forest
}
