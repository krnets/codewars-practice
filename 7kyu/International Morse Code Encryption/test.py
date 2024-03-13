from kata import encryption
import codewars_test as test

@test.it("Basic tests")
def _():
    test.assert_equals(encryption("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
    test.assert_equals(encryption("SOS"), "... --- ...")
    test.assert_equals(encryption("1836"), ".---- ---.. ...-- -....")
    test.assert_equals(encryption("THE QUICK BROWN FOX"), "- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-")
    test.assert_equals(encryption("JUMPED OVER THE"), ".--- ..- -- .--. . -..   --- ...- . .-.   - .... .") 