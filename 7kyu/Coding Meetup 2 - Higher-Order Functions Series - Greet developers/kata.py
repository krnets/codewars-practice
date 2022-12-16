def greet_developers(lst):
    for developer in lst:
        developer["greeting"] = f'Hi {developer["firstName"]}, '
        developer["greeting"] += f'what do you like the most about {developer["language"]}?'
    return lst


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

answer = [
    {
        "firstName": "Sofia",
        "lastName": "I.",
        "country": "Argentina",
        "continent": "Americas",
        "age": 35,
        "language": "Java",
        "greeting": "Hi Sofia, what do you like the most about Java?",
    },
    {
        "firstName": "Lukas",
        "lastName": "X.",
        "country": "Croatia",
        "continent": "Europe",
        "age": 35,
        "language": "Python",
        "greeting": "Hi Lukas, what do you like the most about Python?",
    },
    {
        "firstName": "Madison",
        "lastName": "U.",
        "country": "United States",
        "continent": "Americas",
        "age": 32,
        "language": "Ruby",
        "greeting": "Hi Madison, what do you like the most about Ruby?",
    },
]

import unittest


class SolutionTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(answer, greet_developers(list1))


unittest.main()
