import datetime
import codewars_test as test
from kata import get_villain_name


@test.describe("Example Tests")
def example_tests():
    format_str = "%d/%m/%Y"  # The format
    test.assert_equals(
        get_villain_name(datetime.datetime.strptime("1/1/2000", format_str)),
        "The Evil Pickle",
    )
    test.assert_equals(
        get_villain_name(datetime.datetime.strptime("2/2/2000", format_str)),
        "The Vile Hood Ornament",
    )
    test.assert_equals(
        get_villain_name(datetime.datetime.strptime("2/12/2000", format_str)),
        "The Awkward Hood Ornament",
    )
