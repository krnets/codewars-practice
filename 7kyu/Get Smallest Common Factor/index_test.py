import pytest

from index import scf

EXAMPLES = (
    ('args', 'expected'),
    [
        ([200, 30, 18, 8, 64, 34], 2),
        ([21, 45, 51, 27, 33], 3),
        ([133, 147, 427, 266], 7),
        ([3, 5, 7], 1),
        ([], 1),
    ]
)


@pytest.mark.parametrize(*EXAMPLES)
def test_returns_correct_result(args, expected):
    assert scf(args) == expected
