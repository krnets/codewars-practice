# 7kyu - Javascript filter - 1

""" While developing a website, you detect that some of the members have troubles logging in. 
Searching through the code you find that all logins ending with a "_" make problems. 
So you want to write a function that takes an array of pairs of login-names and e-mails, 
and outputs an array of all login-name, e-mails-pairs from the login-names that end with "_".

If you have the input-array:

[ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]

it should output

[ [ "bar_", "bar@bar.com" ] ]

You have to use the filter-method which returns each element of the array for which the filter-method returns true.

https://docs.python.org/3/library/functions.html#filter """


def search_names(logins):
    return [logins[i] for i in range(len(logins)) if logins[i][0].endswith('_')]


a = [["foo", "foo@foo.com"], ["bar_", "bar@bar.com"]]
q = search_names(a)
q
# [ [ "bar_", "bar@bar.com" ] ]

a = [["foobar_", "foo@foo.com"], ["bar_", "bar@bar.com"]]
q = search_names(a)
q
# [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]

a = [["foo", "foo@foo.com"], ["bar", "bar@bar.com"]]
q = search_names(a)
q
#  []
