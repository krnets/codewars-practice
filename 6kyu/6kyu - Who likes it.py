# 6kyu - Who likes it?

""" You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. 
It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases. """

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


q = likes([])  # 'no one likes this'
q
q = likes(['Peter'])  # 'Peter likes this'
q
q = likes(['Jacob', 'Alex'])  # 'Jacob and Alex like this'
q
q = likes(['Max', 'John', 'Mark'])  # 'Max, John and Mark like this'
q
# 'Alex, Jacob and 2 others like this'
q = likes(['Alex', 'Jacob', 'Mark', 'Max'])
q
