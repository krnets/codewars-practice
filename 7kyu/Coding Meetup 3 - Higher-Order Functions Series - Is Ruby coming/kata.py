def is_ruby_coming(lst):
    return any(x["language"] == "Ruby" for x in lst)


list1 = [
    {
        "firstName": "Sofia",
        "lastName": "I.",
        "country": "Argentina",
        "continent": "Americas",
        "age": 35,
        "language": "Java",
    },
    {
        "firstName": "Lukas",
        "lastName": "X.",
        "country": "Croatia",
        "continent": "Europe",
        "age": 35,
        "language": "Python",
    },
    {
        "firstName": "Madison",
        "lastName": "U.",
        "country": "United States",
        "continent": "Americas",
        "age": 32,
        "language": "Ruby",
    },
]
q = is_ruby_coming(list1)  # True
q

list2 = [
    {
        "firstName": "Sofia",
        "lastName": "I.",
        "country": "Argentina",
        "continent": "Americas",
        "age": 35,
        "language": "Java",
    },
    {
        "firstName": "Lukas",
        "lastName": "X.",
        "country": "Croatia",
        "continent": "Europe",
        "age": 35,
        "language": "Python",
    },
]
q = is_ruby_coming(list2)  # False
q
