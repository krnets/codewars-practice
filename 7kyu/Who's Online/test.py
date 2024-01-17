import codewars_test as test
from kata import who_is_online


@test.describe("Fixed tests")
def fixed_tests():
    @test.it("Simple Cases")
    def example_cases():
        friends = [
            {"username": "David", "status": "online", "last_activity": 10},
            {"username": "Lucy", "status": "offline", "last_activity": 22},
            {"username": "Bob", "status": "online", "last_activity": 104},
        ]
        test.assert_equals(
            who_is_online(friends),
            {"online": ["David"], "offline": ["Lucy"], "away": ["Bob"]},
        )

        friends = [
            {"username": "Lucy", "status": "offline", "last_activity": 22},
            {"username": "Bob", "status": "online", "last_activity": 104},
        ]
        test.assert_equals(
            who_is_online(friends), {"offline": ["Lucy"], "away": ["Bob"]}
        )

        friends = [
            {"username": "David", "status": "online", "last_activity": 10},
            {"username": "Lucy", "status": "offline", "last_activity": 22},
            {"username": "Bob", "status": "online", "last_activity": 104},
        ]
        test.assert_equals(
            who_is_online(friends),
            {"online": ["David"], "offline": ["Lucy"], "away": ["Bob"]},
        )

        friends = [
            {"username": "Lucy", "status": "offline", "last_activity": 22},
            {"username": "Bob", "status": "online", "last_activity": 104},
        ]
        test.assert_equals(
            who_is_online(friends), {"offline": ["Lucy"], "away": ["Bob"]}
        )

        friends = [
            {"username": "David", "status": "online", "last_activity": 10},
            {"username": "Lucy", "status": "online", "last_activity": 0},
            {"username": "Bob", "status": "online", "last_activity": 3},
            {"username": "Julie", "status": "offline", "last_activity": 104},
            {"username": "Lenny", "status": "online", "last_activity": 38},
        ]
        test.assert_equals(
            who_is_online(friends),
            {
                "online": ["David", "Lucy", "Bob"],
                "offline": ["Julie"],
                "away": ["Lenny"],
            },
        )

        friends = [
            {"username": "David", "status": "online", "last_activity": 10},
            {"username": "Lucy", "status": "online", "last_activity": 0},
            {"username": "Bob", "status": "offline", "last_activity": 104},
            {"username": "Julie", "status": "online", "last_activity": 3},
            {"username": "Lenny", "status": "online", "last_activity": 38},
            {"username": "Charlie", "status": "online", "last_activity": 34},
            {"username": "Jemma", "status": "offline", "last_activity": 2},
            {"username": "Tom", "status": "online", "last_activity": 11},
            {"username": "Tommy", "status": "online", "last_activity": 9},
            {"username": "Jonny", "status": "online", "last_activity": 4},
            {"username": "Natalie", "status": "offline", "last_activity": 97},
        ]
        test.assert_equals(
            who_is_online(friends),
            {
                "online": ["David", "Lucy", "Julie", "Tommy", "Jonny"],
                "offline": ["Bob", "Jemma", "Natalie"],
                "away": ["Lenny", "Charlie", "Tom"],
            },
        )

        friends = []
        test.assert_equals(who_is_online(friends), {})
