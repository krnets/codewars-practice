import codewars_test as test
from kata import gym_slang

test.describe("Basic tests")
test.it("should work for the quotes shown above in the picture")
test.assert_equals(gym_slang("When I miss few days of gym"), "When I miss few days of gym")
test.assert_equals(gym_slang("Squad probably think I am fake"), "Squad prolly think I'm fake")
test.assert_equals(gym_slang("Whole squad probably bigger than me now"), "Whole squad prolly bigger than me now")
test.assert_equals(gym_slang("No selfie to post on Instagram either"), "No selfie to post on Insta either")
test.assert_equals(gym_slang("Gym crush probably found someone else"), "Gym crush prolly found someone else")
test.assert_equals(gym_slang("What if I die fat"), "What if I die fat")
test.assert_equals(gym_slang("What if I do not fit in my clothes now"), "What if I don't fit in my clothes now")
test.assert_equals(gym_slang("Going to feel like a new gym member"), "Gonna feel like a new gym member")
test.assert_equals(gym_slang("wait what was my lock combination"), "wait what was my lock combo")
test.assert_equals(gym_slang("that skinny girl can probably outlift me now"), "that skinny girl can prolly outlift me now")

test.it("should work for both lowercase and capitalized examples")
test.assert_equals(gym_slang("probably Probably"), "prolly Prolly")
test.assert_equals(gym_slang("i am I am"), "i'm I'm")
test.assert_equals(gym_slang("instagram Instagram"), "insta Insta")
test.assert_equals(gym_slang("do not Do not"), "don't Don't")
test.assert_equals(gym_slang("going to Going to"), "gonna Gonna")
test.assert_equals(gym_slang("combination Combination"), "combo Combo")

test.it("should find and replace <b><i><u>all</u></i></b> instances of keywords")
test.assert_equals(gym_slang("probably Probably probably Probably probably Probably probably Probably probably Probably"), "prolly Prolly prolly Prolly prolly Prolly prolly Prolly prolly Prolly")
test.assert_equals(gym_slang("i am I am i am I am i am I am i am I am i am I am i am I am"), "i'm I'm i'm I'm i'm I'm i'm I'm i'm I'm i'm I'm")
test.assert_equals(gym_slang("instagram Instagram instagram Instagram instagram Instagram instagram Instagram instagram Instagram"), "insta Insta insta Insta insta Insta insta Insta insta Insta")
test.assert_equals(gym_slang("do not Do not do not Do not do not Do not do not Do not"), "don't Don't don't Don't don't Don't don't Don't")
test.assert_equals(gym_slang("Going to going to Going to Going to going to Going to Going to going to Going to"), "Gonna gonna Gonna Gonna gonna Gonna Gonna gonna Gonna")
test.assert_equals(gym_slang("combination combination Combination combination Combination"), "combo combo Combo combo Combo")