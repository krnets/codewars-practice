from kata import name_score
import codewars_test as test

@test.describe("Basic tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(name_score('Mary Jane'), {"Mary Jane":20})
        test.assert_equals(name_score('Luke Skywalker'), {"Luke Skywalker":41})
        test.assert_equals(name_score('Zoe Andrews'), {"Zoe Andrews":23})
        test.assert_equals(name_score('Double  Space'), {"Double  Space":25})
        test.assert_equals(name_score('Greg Z MacDonald'), {"Greg Z MacDonald":26})