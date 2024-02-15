import codewars_test as test
from kata import ride
import codewars_test as test

@test.it('Basic Tests')
def _():
    group = "COMETQ"
    comet = "HVNGAT"
    test.assert_equals(ride(group,comet),"GO")

    group = "STARAB"
    comet = "USACO"
    test.assert_equals(ride(group,comet),"STAY")
