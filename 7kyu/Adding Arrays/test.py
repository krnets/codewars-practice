import codewars_test as test
from kata import arr_adder

@test.describe('Testing')
def _():

    @test.it("Example tests")
    def example_tests():
        test.assert_equals(arr_adder([
            ['J','L','L','M'],
            ['u','i','i','a'],
            ['s','v','f','n'],
            ['t','e','e','' ]
        ]),"Just Live Life Man")
        test.assert_equals(arr_adder([
            ['T','M','i','t','p','o','t','c'],
            ['h','i','s','h','o','f','h','e'],
            ['e','t','', 'e','w','', 'e','l'],
            ['', 'o','', '', 'e','', '', 'l'],
            ['', 'c','', '', 'r','', '', '' ],
            ['', 'h','', '', 'h','', '', '' ],
            ['', 'o','', '', 'o','', '', '' ],
            ['', 'n','', '', 'u','', '', '' ],
            ['', 'd','', '', 's','', '', '' ],
            ['', 'r','', '', 'e','', '', '' ],
            ['', 'i','', '', '', '', '', '' ],
            ['', 'a','', '', '', '', '', '' ]
        ]), "The Mitochondria is the powerhouse of the cell");
