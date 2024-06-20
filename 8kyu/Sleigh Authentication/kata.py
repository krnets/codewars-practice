import hashlib
import codewars_test as test


class Sleigh(object):
    def __init__(self) -> None:
        self.username = "Santa Claus"
        self.salt = "85ead9346c124214af8ac549f95430f6"
        self.encoded_pwd = hashlib.sha512(
            ("Ho Ho Ho!" + self.salt).encode()
        ).hexdigest()

    def authenticate(self, name, password) -> bool:
        return (name == self.username
            and hashlib.sha512((password + self.salt).encode()).hexdigest()
            == self.encoded_pwd)


test.describe("Santa's Sleigh")

sleigh = Sleigh()


def test_credentials(name, password, expected):
    test.assert_equals(
        sleigh.authenticate(name, password),
        expected,
        "Tested name %s and password %s" % (name, password),
    )


test.it("must authenticate with correct credentials")
test_credentials("Santa Claus", "Ho Ho Ho!", True)

test.it("Must not authenticate with incorrect credentials")
test_credentials("Santa", "Ho Ho Ho!", False)
test_credentials("Santa Claus", "Ho Ho!", False)
test_credentials("jhoffner", "CodeWars", False)
