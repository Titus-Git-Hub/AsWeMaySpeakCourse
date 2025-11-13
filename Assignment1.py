import tracery
from tracery.modifiers import base_english

rules = {
    "origin": "#zoo# #p1# #p2# #time# unluckily #number# #p3# #news#",
    "zoo": ["Lüneburg Zoo:", "Hamburg Zoo:", "Berlin Zoo:",
            "Munich Zoo:", "Bonn Zoo"],
    "p1": ["We must admit that while", "We are sorry to tell that while",
           "While", "Today, while"],
    "p2": ["cleaning the #animal# compound"],
    "time": ["at 11AM,", "at 12AM,", "at 1PM,", "at 2PM,",
             "at 3PM,", "at 4PM,", "at 5PM,"],
    "number": ["2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "p3": ["of our #animal.s#"],
    "news": ["were able to escape.", "got kidnapped.", "died unexpectedly.",
             "caused quite a bit of noise in the surrounding area.",
             "unexpectedly attacked visitors."],
    "animal": ["Crocodile", "Snake", "Flamingo", "Leopard", "Elephant",
               "Zebra", "Tiger", "Lion", "Chimpanzee", "Eagle"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

for i in range(10):
    print(grammar.flatten("#origin#"))
