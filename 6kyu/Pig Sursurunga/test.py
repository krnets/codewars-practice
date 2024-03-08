import codewars_test as test
from kata import sursurungal
test.describe("Some basic tests : ")
test.assert_equals(sursurungal("1 tomato"),"1 tomato")
test.assert_equals(sursurungal("0 tomato"),"0 tomato","0 is considered as singular")
test.assert_equals(sursurungal("1 ananas"),"1 ananas","singular ending with 's' keep it")
  
test.assert_equals(sursurungal("2 bananas"),"2 bubanana","dual should start with 'bu'")
test.assert_equals(sursurungal("3 bananas"),"3 bananazo","paucal should end with 'zo'")
test.assert_equals(sursurungal("10 bananas"),"10 gabananaga","plural should start and end with 'ga'" )
test.assert_equals(sursurungal("111 bananas"),"111 gabananaga","111 is a plural, not a singular")