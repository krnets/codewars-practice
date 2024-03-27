import codewars_test as test
from kata import compare_versions


def dotest(v1, v2, expected):
    test.assert_equals(compare_versions(v1, v2), expected, f"With version = {v1}, version2 = {v2}")


@test.describe("Sample tests")
def test_group():
    for v1, v2, expected, title in (
            ("11", "10", True, 'Testing versions without subversion'),
            ("11", "11", True, 'Test equal versions'),
            ("10.4.6", "10.4", True, 'Adding a subversion should make this version "larger"'),
            ("10.4", "10.4.8", False, 'Adding a subversion should make this version "larger"'),
            ("10.4", "11", False, 'Subversion precedence is smaller than Version'),
            ("10.4", "10.10", False, 'Version value is not the same as its decimal value'),
            ("10.4.9", "10.5", False, 'Adding subversion does not make it larger than a greater version'),
    ):
        @test.it(title)
        def single_test():
            dotest(v1, v2, expected)
