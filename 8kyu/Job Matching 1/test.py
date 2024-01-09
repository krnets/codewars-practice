from solution import match
import codewars_test as test

test.describe("Basic tests")
candidate1 = { 'min_salary': 120000 }
candidate2 = { 'min_salary': 190000 }
job1 = { 'max_salary': 130000 }
job2 = { 'max_salary': 80000 }
job3 = { 'max_salary': 171000 }

test.it('should detect valid matches')
test.assert_equals(match(candidate1, job1), True)
test.assert_equals(match(candidate1, job3), True)
test.assert_equals(match(candidate2, job3), True)

test.it('should detect invalid matches')
test.assert_equals(match(candidate1, job2), False)
test.assert_equals(match(candidate2, job1), False)
test.assert_equals(match(candidate2, job2), False)

test.it('should throw when a candidate has no min_salary')
test.expect_error("Should throw error", lambda a: match({}, job2))

test.it('should throw when a job has no max_salary')
test.expect_error("Should throw error", lambda a: match(candidate1, {}))

test.describe("Random tests")
from random import randint
sol=lambda c, j: j['max_salary']>=c['min_salary']*0.9 if 'max_salary' in j and 'min_salary' in c else [].pippi()
c={};j={}

for _ in range(40):
    j['max_salary']=(randint(1,75)+50)*1000; c['min_salary']=(randint(1,100)+75)*1000
    test.it("Testing for %s and %s" %(c,j))
    test.assert_equals(match(c, j),sol(c, j),"It should work for random inputs too")