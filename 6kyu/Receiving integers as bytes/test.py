import codewars_test as test
from kata import interpret_as_int32

cases = [
    ([b"\0\0\0\0"], [0]),
    ([b"\0\0\0\1"], [1]),
    ([b"\x7f\xff\xff\xff"], [2147483647]),
    ([b"\xff\xff\xff\xff"], [-1]),
    ([b"\x80\0\0\0"], [-2147483648]),
    ([b""], []),
    ([], []),
    ([b"\0"], []),
    ([b"\0\0\1", b"\1\0"], [257]),
    ([b"\0\0", b"", b"\0\1"], [1]),
    ([b"\0", b"\0", b"\1", b"\0"], [256]),
    (
        [
            b"$\x99\x9fy\x81\xdc\x8bLWg`",
            b"SJX\xeeB\x01\xbaD\xda\xf7<\xbe#\x1c\xf1p\xdf\xe5\x05\xb1\xb2A\xe6\x83\x9a\x9e\xa1C\x1fv\xdfbI\x93\x7f\x07sr\xb1\x99p\x193\xf9zo\x0e\x07\xa7\xd5G\x0fO>\xc1Ry\x94\xca\xc59\xcaX:\x1f\x87\xf2t\xd1",
        ],
        [
            614047609,
            -2116252852,
            1466392659,
            1247342146,
            28984538,
            -147014109,
            485585119,
            -452611662,
            1105626010,
            -1633598689,
            1994351177,
            -1820391565,
            1924241776,
            422836602,
            1863190439,
            -716763313,
            1052856953,
            -1798650567,
            -900187617,
            -2014153519,
        ],
    ),
]

for input_, output in cases:
    test.assert_equals(interpret_as_int32(input_), output)
