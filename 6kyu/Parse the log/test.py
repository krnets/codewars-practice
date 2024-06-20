import codewars_test as test
import re

# logparser = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+(ERROR|INFO)\s+\[(\w+):(\w+):?(\w+)?\]\s+(.+)"

# logparser = ("(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+"
#              "(ERROR|INFO)\s+"
#              "\[(\w+):(\w+):?(\w+)?\]\s+"
#              "(.+)")

logparser = ("(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s+"  # Date parsing
             "(ERROR|INFO)\s+"  # Error level
             "\[(\w+):(\w+):?(\w+)?\]\s+"  # User, Function, Subfunction
             "(.+)")  # Error message

regex = re.compile(logparser)

test.assert_equals(
    regex.findall(
        "2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] We have a problem"
    ),
    [
        (
            "2003-07-08 16:49:45,896",
            "ERROR",
            "user1",
            "mainfunction",
            "subfunction",
            "We have a problem",
        )
    ],
    "Valid Line",
)
test.assert_equals(
    regex.findall(
        "2003-07-08 16:49:46,896 INFO [user1:mainfunction] We don't have a problem"
    ),
    [
        (
            "2003-07-08 16:49:46,896",
            "INFO",
            "user1",
            "mainfunction",
            "",
            "We don't have a problem",
        )
    ],
    "Valid Line",
)
test.assert_equals(
    len(
        regex.findall(
            "2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] We have a problem"
        )[0]
    ),
    6,
    "Didn't find all the groups",
)

test.assert_equals(
    regex.findall(
        "2007-07-08 26:49:46,805 INFO     [user1:mainfunction] We have a problem"
    ),
    [
        (
            "2007-07-08 26:49:46,805",
            "INFO",
            "user1",
            "mainfunction",
            "",
            "We have a problem",
        )
    ],
)


test.assert_equals(
    regex.findall(
        "2013-12-08 10:49:46,492      INFO [user1:mainfunction] We have a problem"
    ),
    [
        (
            "2013-12-08 10:49:46,492",
            "INFO",
            "user1",
            "mainfunction",
            "",
            "We have a problem",
        )
    ],
)

test.assert_equals(
    regex.findall(
        "2703-07-08 13:39:46,693 INFO [user1:mainfunction:thing]     We have a problem"
    ),
    [
        (
            "2703-07-08 13:39:46,693",
            "INFO",
            "user1",
            "mainfunction",
            "thing",
            "We have a problem",
        )
    ],
)
