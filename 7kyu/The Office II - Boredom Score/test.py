from kata import boredom
import codewars_test as test


@test.it("Basic tests")
def basic_tests():
    test.assert_equals(
        boredom(
            {
                "tim": "change",
                "jim": "accounts",
                "randy": "canteen",
                "sandy": "change",
                "andy": "change",
                "katie": "IS",
                "laura": "change",
                "saajid": "IS",
                "alex": "trading",
                "john": "accounts",
                "mr": "finance",
            }
        ),
        "kill me now",
    )
    test.assert_equals(
        boredom(
            {
                "tim": "IS",
                "jim": "finance",
                "randy": "pissing about",
                "sandy": "cleaning",
                "andy": "cleaning",
                "katie": "cleaning",
                "laura": "pissing about",
                "saajid": "regulation",
                "alex": "regulation",
                "john": "accounts",
                "mr": "canteen",
            }
        ),
        "i can handle this",
    )
    test.assert_equals(
        boredom(
            {
                "tim": "accounts",
                "jim": "accounts",
                "randy": "pissing about",
                "sandy": "finance",
                "andy": "change",
                "katie": "IS",
                "laura": "IS",
                "saajid": "canteen",
                "alex": "pissing about",
                "john": "retail",
                "mr": "pissing about",
            }
        ),
        "party time!!",
    )
