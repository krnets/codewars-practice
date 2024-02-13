import codewars_test as test
from kata import oper, rot, selfie_and_rot


# Helper function to run tests
def run_test(function, input_str, expected_output_str):
    result = oper(function, input_str)
    expected_output = expected_output_str.split("\n")
    test.assert_equals(result.split("\n"), expected_output)


# Test cases for the 'rot' function
@test.describe("rot")
def rot_tests():
    @test.it("Basic tests rot")
    def basic_test_cases():
        run_test(
            rot,
            "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL",
            "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif",
        )
        run_test(rot, "rkKv\ncofM\nzXkh\nflCB", "BClf\nhkXz\nMfoc\nvKkr")
        run_test(rot, "lVHt\nJVhv\nCSbg\nyeCt", "tCey\ngbSC\nvhVJ\ntHVl")
        run_test(rot, "QMxo\ntmFe\nWLUG\nowoq", "qowo\nGULW\neFmt\noxMQ")


# Test cases for the 'selfie_and_rot' function
@test.describe("selfie_and_rot")
def selfie_and_rot_tests():
    @test.it("Basic tests selfie_and_rot")
    def basic_test_cases():
        run_test(
            selfie_and_rot,
            "xZBV\njsbS\nJcpN\nfVnP",
            "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx",
        )
        run_test(
            selfie_and_rot,
            "uLcq\nJkuL\nYirX\nnwMB",
            "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu",
        )
        run_test(
            selfie_and_rot,
            "lVHt\nJVhv\nCSbg\nyeCt",
            "lVHt....\nJVhv....\nCSbg....\nyeCt....\n....tCey\n....gbSC\n....vhVJ\n....tHVl",
        )
        run_test(
            selfie_and_rot,
            "QMxo\ntmFe\nWLUG\nowoq",
            "QMxo....\ntmFe....\nWLUG....\nowoq....\n....qowo\n....GULW\n....eFmt\n....oxMQ",
        )
