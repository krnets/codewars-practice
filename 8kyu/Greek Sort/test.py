from solution import greek_comparator
import codewars_test as test

test.expect(greek_comparator('alpha', 'beta') < 0, "result should be negative")
test.assert_equals(greek_comparator('psi', 'psi'), 0)
test.expect(greek_comparator('upsilon', 'rho'), "result should be positive")