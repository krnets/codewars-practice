import pytest

from index import graceful_tipping

EXAMPLES = (
    ('args', 'expected'),
    [
        ((1), 2),
        ((7), 9),
        ((12), 15),
        ((86), 100),
        ((99), 150),
        ((1149), 1500),
        ((983212), 1500000)

    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert graceful_tipping(args) == expected
