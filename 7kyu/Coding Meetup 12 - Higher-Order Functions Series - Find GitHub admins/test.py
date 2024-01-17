import codewars_test as test
from kata import find_admin


@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        list1 = [
            {
                "firstName": "Harry",
                "lastName": "K.",
                "country": "Brazil",
                "continent": "Americas",
                "age": 22,
                "language": "JavaScript",
                "githubAdmin": "yes",
            },
            {
                "firstName": "Kseniya",
                "lastName": "T.",
                "country": "Belarus",
                "continent": "Europe",
                "age": 49,
                "language": "Ruby",
                "githubAdmin": "no",
            },
            {
                "firstName": "Jing",
                "lastName": "X.",
                "country": "China",
                "continent": "Asia",
                "age": 34,
                "language": "JavaScript",
                "githubAdmin": "yes",
            },
            {
                "firstName": "Piotr",
                "lastName": "B.",
                "country": "Poland",
                "continent": "Europe",
                "age": 128,
                "language": "JavaScript",
                "githubAdmin": "no",
            },
        ]

        answer1 = [
            {
                "firstName": "Harry",
                "lastName": "K.",
                "country": "Brazil",
                "continent": "Americas",
                "age": 22,
                "language": "JavaScript",
                "githubAdmin": "yes",
            },
            {
                "firstName": "Jing",
                "lastName": "X.",
                "country": "China",
                "continent": "Asia",
                "age": 34,
                "language": "JavaScript",
                "githubAdmin": "yes",
            },
        ]

        test.assert_equals(find_admin(list1, "JavaScript"), answer1)
        test.assert_equals(find_admin(list1, "Ruby"), [])
        test.assert_equals(find_admin(list1, "Python"), [])
