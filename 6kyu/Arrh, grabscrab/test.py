import codewars_test as test
from kata import grabscrab


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Tests")
    def _():
        cases = [
            ("trisf", ["first"], ["first"]),
            ("oob", ["bob", "baobab"], []),
            ("ainstuomn", ["mountains", "hills", "mesa"], ["mountains"]),
            ("oolp", ["donkey", "pool", "horse", "loop"], ["pool", "loop"]),
            ("ortsp", ["sport", "parrot", "ports", "matey"], ["sport", "ports"]),
            ("ourf", ["one", "two", "three"], []),
            ("racer", ["crazer", "carer", "racar", "caers", "racer"], ["carer", "racer"]),
            ("abba", ["aabb", "abcd", "bbaa", "abbb", "aaab"], ["aabb", "bbaa"]),
        ]
        for said, possible_words, expected in cases:
            msg = f"Incorrect answer for:\n  word = {repr(said)}\n  words = {repr(possible_words)}\n"
            test.assert_equals(grabscrab(said, possible_words), expected, msg)