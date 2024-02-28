import codewars_test as test
from kata import compose


@test.describe("Fixed Tests")
def fixed_tests():
    def testing(actual, expected):
        test.assert_equals(actual, expected)

    @test.it("Basic Test Cases")
    def basic_test_cases():
        testing(
            compose("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB"),
            "bNkTB\nhTrWO\nRTFVi\nCnnIj",
        )
        testing(
            compose("HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW"),
            "HgYPW\nTGGbM\nIPhqt\nuUMDH",
        )
        testing(
            compose("tSrJ\nOONy\nsqPF\nxMkB", "hLqw\nEZuh\nmYFl\nzlYf"),
            "tzlYf\nOOmYF\nsqPEZ\nxMkBh",
        )
        testing(compose("fn\nlr", "Kz\nmO"), "fmO\nlrK")
        testing(
            compose(
                "fctRKq\nBCorKQ\nZKGbDO\nbhHohe\nUjyNSg\nPCOiuM",
                "elSYAB\nLQMYuN\nTzQtaM\nFutqip\nwSAjZX\nuOPhSJ",
            ),
            "fuOPhSJ\nBCwSAjZ\nZKGFutq\nbhHoTzQ\nUjyNSLQ\nPCOiuMe",
        )

        testing(
            compose("qtKz\negiP\niOgb\nRqly", "ZUCx\nShBJ\nmybK\neBZA"),
            "qeBZA\negmyb\niOgSh\nRqlyZ",
        )
        testing(
            compose("rmNE\naFQJ\nfsNe\ntDtw", "GvqU\noJlZ\ngJxQ\nVQvX"),
            "rVQvX\naFgJx\nfsNoJ\ntDtwG",
        )
        testing(
            compose("RCKr\naJwU\nqEyM\nNbdP", "hxYA\nlUtD\nLFmc\nssTy"),
            "RssTy\naJLFm\nqEylU\nNbdPh",
        )
        testing(
            compose(
                "lFqaEC\nITEzHC\nqaEPEb\nexhzgU\nxoxRJc\nTxqlDN",
                "IMpAnn\nktLyDb\nHawiQt\nNVRips\ncrKROc\nJqPpty",
            ),
            "lJqPpty\nITcrKRO\nqaENVRi\nexhzHaw\nxoxRJkt\nTxqlDNI",
        )
        testing(
            compose("wEGa\nhICc\nPrvY\nCuSd", "qfYz\nwJfU\noHhO\nNxaV"),
            "wNxaV\nhIoHh\nPrvwJ\nCuSdq",
        )
