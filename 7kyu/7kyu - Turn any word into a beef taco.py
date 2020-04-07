# 7kyu - Turn any word into a beef taco

""" If you like Taco Bell, you will be familiar with their signature doritos locos taco. They're very good.

Why can't everything be a taco? We're going to attempt that here, turning every word we find 
into the taco bell recipe with each ingredient.

We want to input a word as a string, and return a list representing that word as a taco.

Key

all vowels (except 'y') = beef

t = tomato
l = lettuce
c = cheese
g = guacamole
s = salsa

NOTE
We do not care about case here. 
'S' is therefore equivalent to 's' in our taco.

Ignore all other letters; 
we don't want our taco uneccesarily clustered or else it will be too difficult to eat.

Note that no matter what ingredients are passed, our taco will always have a shell. """

# import re

# def tacofy(word):
#     ingredients = dict(t='tomato', l='lettuce', c='cheese', g='guacamole', s='salsa')
#     word = re.sub(r'[^aeioutlcgs]', '', word.lower())
#     taco = ['beef' if x in 'aeiou' else ingredients[x] for x in word]
#     taco.insert(0, 'shell')
#     taco.append('shell')
#     return taco


def tacofy(word):
    ingredients = dict(t='tomato', l='lettuce', c='cheese', g='guacamole', s='salsa')
    return ['shell'] + [ingredients.get(c, 'beef') for c in word.lower() if c in 'aeioutlcgs'] + ['shell']


q = tacofy("")  # ['shell', 'shell']
q
q = tacofy("a")  # ['shell', 'beef', 'shell']
q
q = tacofy("ggg")  # ['shell', 'guacamole', 'guacamole', 'guacamole', 'shell']
q
q = tacofy("ogl")  # ['shell', 'beef', 'guacamole', 'lettuce', 'shell']
q
q = tacofy("ydjkpwqrzto")  # ['shell', 'tomato', 'beef', 'shell']
q
