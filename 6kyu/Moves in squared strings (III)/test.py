import codewars_test as test
from kata import *


def testing(actual, expected):
    test.assert_equals(actual, expected)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic tests rot_90_clock")
    def basic_test_cases():
        testing(
            oper(rot_90_clock, "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb"),
            "Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle",
        )

    @test.it("Basic tests diag_1_sym")
    def basic_test_cases():
        testing(
            oper(diag_1_sym, "wuUyPC\neNHWxw\nehifmi\ntBTlFI\nvWNpdv\nIFkGjZ"),
            "weetvI\nuNhBWF\nUHiTNk\nyWflpG\nPxmFdj\nCwiIvZ",
        )

    @test.it("Basic tests selfie_and_diag1")
    def basic_test_cases():
        testing(
            oper(selfie_and_diag1, "NJVGhr\nMObsvw\ntPhCtl\nsoEnhi\nrtQRLK\nzjliWg"),
            "NJVGhr|NMtsrz\nMObsvw|JOPotj\ntPhCtl|VbhEQl\nsoEnhi|GsCnRi\nrtQRLK|hvthLW\nzjliWg|rwliKg",
        )
