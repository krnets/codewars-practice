""" 6kyu - Santa's Missing Gift List

Santa has misplaced his list of gift to all the children, he has however a condensed version lying around.

In this condensed verison, instead of a list of gifts for each child, each one has an integer.

He also have a list of gifts corresponding to each integer. His list is as follows:

GIFTS = {
  1: 'Toy Soldier',
  2: 'Wooden Train',
  4: 'Hoop',
  8: 'Chess Board',
  16: 'Horse',
  32: 'Teddy',
  64: 'Lego',
  128: 'Football',
  256: 'Doll',
  512: "Rubik's Cube"
}

This list is made available to you, as GIFTS.

The integer for each child is such that the child should get the highest toy 
lower than or equal to that integer, and then, if there's more left, 
also get the highest toy lower than the rest and so on. 
Know that Santa never gives the same gift twice.

For example, by Timmy's name is 160. This means that Timmy should get both a football and a teddy, because 128 + 32 = 160.

You should help Santa by decoding his own list and recreate the missing list for him. 
Santa's elf wants the list sorted alphabetically by the toys, so you should help them as well and list the toys in a sorted order. """

GIFTS = {
    1: 'Toy Soldier',
    2: 'Wooden Train',
    4: 'Hoop',
    8: 'Chess Board',
    16: 'Horse',
    32: 'Teddy',
    64: 'Lego',
    128: 'Football',
    256: 'Doll',
    512: "Rubik's Cube"
}


# def gifts(number):
#     result = []
#     toy_id = [2**i for i in range(10, 0, -1)] + [1]
#     for i in range(len(toy_id)):
#         if toy_id[i] <= number:
#             result.append(toy_id[i])
#             number -= toy_id[i]
#     return sorted(GIFTS.get(x) for x in result)

# def gifts(number):
#     return sorted(GIFTS[k] for k, v in GIFTS.items() if k & number)

# def gifts(number):
#     return sorted(GIFTS[2**i] for i, x in enumerate(reversed(bin(number))) if x == '1')

def gifts(number):
    return sorted(GIFTS[1 << i] for i, x in enumerate(reversed(bin(number))) if x == '1')


q = gifts(1), ['Toy Soldier']
q
q = gifts(2), ['Wooden Train']
q
q = gifts(3), ['Toy Soldier', 'Wooden Train']
q
q = gifts(22), ['Hoop', 'Horse', 'Wooden Train']
q
q = gifts(160), ['Football', 'Teddy']
q
