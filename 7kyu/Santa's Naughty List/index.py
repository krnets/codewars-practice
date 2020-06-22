""" 7kyu - Santa's Naughty List

Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the big day. 
Go through a list of children, and return a list containing every child who appeared on Santa's list. 
Do not add any child more than once. Output should be sorted.

Comparison should be case sensitive and the returned list should contain only one copy of each name: 
"Sam" and "sam" are different, but "sAm" and "sAm" are not. """


def find_children(santas_list, children):
    return sorted(set(santas_list).intersection(children))


q = find_children(["Jason", "Jackson", "Jordan", "Johnny"], [
                  "Jason", "Jordan", "Jennifer"])  # ["Jason", "Jordan"]
q
q = find_children(["Jason", "Jackson", "Johnson", "JJ"], [
                  "Jason", "James", "JJ"])  # ["JJ", "Jason"]
q
q = find_children(["jASon", "JAsoN", "JaSON", "jasON"], [
                  "JasoN", "jASOn", "JAsoN", "jASon", "JASON"])  # ["JAsoN", "jASon"]
q
