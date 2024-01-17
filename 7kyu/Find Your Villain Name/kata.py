import datetime

first = [ "The Evil", "The Vile", "The Cruel", "The Trashy", "The Despicable", "The Embarrassing",
    "The Disreputable", "The Atrocious", "The Twirling", "The Orange", "The Terrifying", "The Awkward", ]
last = [ "Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", 
        "House Cat", "Teaspoon", "Laundry Basket", ]

def get_villain_name(birthdate: datetime) -> str:
    return first[birthdate.month - 1] + " " + last[birthdate.day % 10]
