import codewars_test as test
from kata import sol


@test.describe("Example test cases")
def sample_tests():
    test.assert_equals(sol(["apple", "application", "appearance"]), "app")
    test.assert_equals(sol(["orange", "organic", "origami", "ore"]), "or")
    test.assert_equals(sol(["code", "coding", "codewars", "codomain"]), "cod")
    test.assert_equals(sol(["why", "what", "who", "which", "where", "how"]), "")
    test.assert_equals(sol(["11", "12", "13", "14", "15"]), "1")
    test.assert_equals(sol(["16", "17", "18", "19", "20"]), "")
    test.assert_equals(sol(["cba", "dcba", "edcba", "fedcba", "gfedcba"]), "")
    test.assert_equals(sol(["wwwwww", "wwwwww", "wwwwww", "wwwwww", "mmmmmm"]), "")
    test.assert_equals(sol(["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027"]), "20")
    test.assert_equals(sol(["abc", "abcd", "abcde", "abcdef", "abcdefg"]), "abc")
    test.assert_equals(sol(["wwwwww", "wwww", "www", "wwwwww", "wwwwww"]), "www")
    test.assert_equals(sol(["wwwwww", "wwwwww", "wwwwww", "wwwwww", "wwwwww"]), "wwwwww")
