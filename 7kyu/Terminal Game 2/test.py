from kata import move
import codewars_test as test


test.describe("The move function")
myHero = Hero()

test.it("should work for correct input")
test.assert_equals(myHero.position, '00')
myHero.move('down')
test.assert_equals(myHero.position, '10')
myHero.move('right')
test.assert_equals(myHero.position, '11')
myHero.move('up')
test.assert_equals(myHero.position, '01')
myHero.move('right')
test.assert_equals(myHero.position, '02')

for i in range(1, 5):
    myHero.move("down")
    test.assert_equals(myHero.position, str(i) + "2")

test.it("should throw error if the new position is out of bounds")
test.expect_error("Didn't throw an expected error", lambda: Hero().move('up'))
test.expect_error("Didn't throw an expected error", lambda: Hero().move('left'))
test.expect_error("Didn't throw an expected error", lambda: myHero.move('down'))

test.it("should not modify position in case of bad input")
test.assert_equals(myHero.position, "42")