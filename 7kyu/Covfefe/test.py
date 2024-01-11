from kata import covfefe
import codewars_test as test


@test.it("basic tests")
def _():
    test.assert_equals(covfefe("coverage"),"covfefe")
    test.assert_equals(covfefe("coverage coverage"),"covfefe covfefe")
    test.assert_equals(covfefe("nothing"),"nothing covfefe")
    test.assert_equals(covfefe("double space "),"double space  covfefe")
    test.assert_equals(covfefe("covfefe"),"covfefe covfefe")
    test.assert_equals(covfefe("erag"),"erag covfefe")
