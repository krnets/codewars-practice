import codewars_test as test
from kata import create_message

test.assert_equals(
    create_message("Hello")("World!")("how")("are")("you?")(),
    "Hello World! how are you?",
)
