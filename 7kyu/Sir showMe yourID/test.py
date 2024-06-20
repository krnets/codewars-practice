import codewars_test as test
from kata import show_me

test.describe("Basic tests")
test.assert_equals(show_me("Francis"), True, "Francis is a name !")
test.assert_equals(show_me("Jean-Eluard"), True, "Jean-Eluard is a name!")
test.assert_equals(show_me("Le Mec"), False, "Le Mec is not a name!")
test.assert_equals(show_me("Bernard-Henry-Levy"), True, "Bernard-Henry-Levy is a name!")
test.assert_equals(show_me("Meme Gertrude"), False, "Meme Gertrude is not a name! It's my Grandma ")
test.assert_equals(show_me("A-a-a-a----a-a"), False)
test.assert_equals(show_me("Z-------------"), False)
test.assert_equals(show_me("Jean-luc"), False)
test.assert_equals(show_me("Jean--Luc"), False)
test.assert_equals(show_me("JeanLucPicard"), False)
test.assert_equals(show_me("-Jean-Luc"), False)
test.assert_equals(show_me("Jean-Luc-Picard-"), False)
