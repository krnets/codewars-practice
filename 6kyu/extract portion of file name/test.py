import codewars_test as test
from kata import *


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            FileNameExtractor.extract_file_name(
                "1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"
            ),
            "FILE_NAME.EXTENSION",
        )
        test.assert_equals(
            FileNameExtractor.extract_file_name(
                "1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"
            ),
            "FILE_NAME.EXTENSION",
        )
        test.assert_equals(
            FileNameExtractor.extract_file_name(
                "1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34"
            ),
            "This_is_an_otherExample.mpg",
        )
        test.assert_equals(
            FileNameExtractor.extract_file_name("1231231223123131_myFile.tar.gz2"),
            "myFile.tar",
        )
