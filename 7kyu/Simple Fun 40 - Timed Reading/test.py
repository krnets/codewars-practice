import codewars_test as test
from kata import timed_reading

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(timed_reading(4, "The Fox asked the stork, 'How is the soup?'"), 7)
        test.assert_equals(timed_reading(1, "..."), 0)
        test.assert_equals(timed_reading(3, "This play was good for us."), 3)
        test.assert_equals(timed_reading(3, "Suddenly he stopped, and glanced up at the houses"), 5)
        test.assert_equals(timed_reading(6, "Zebras evolved among the Old World horses within the last four million years."), 11)
        test.assert_equals(timed_reading(5, "Although zebra species may have overlapping ranges, they do not interbreed."), 6)
        test.assert_equals(timed_reading(1, "Oh!"), 0)
        test.assert_equals(timed_reading(5, "Now and then, however, he is horribly thoughtless, and seems to take a real delight in giving me pain."), 14)

        test.assert_equals(timed_reading(4, 'FvjoHzI zhEqlSTHAa ZHJsprV mJuF hWVgCOKs WUt eWUqRBmf MgjqhQtZgiB RkAuRGzY mSyxp FbJuHW gEjUPbyXBw kuSNZFQO iRgZtyVUUfu sVo Eb zJlqJQcGDGH DXN'), 5)
        test.assert_equals(timed_reading(5, 'LRHhMMu wBAiqCU jSVXJadwY aKAgAva Na hCfLvPcR vmSHwsjht Iwsn RiLPJWj HXvnP RCujP cz chcey CtpBCkjiEy AKVllKhQMh OLA WImf DbAY'), 9)