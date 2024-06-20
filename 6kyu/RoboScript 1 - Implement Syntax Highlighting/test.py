import codewars_test as test
from kata import highlight

message = "Given Code: {}\n\nResults"
@test.describe("Your Syntax Highlighter")
def syntax_highlighter():
    @test.it("Should work for the provided examples")
    def examples():
        code = "FFFR345F2LL"
        expected = '<span style="color: pink">FFF</span><span style="color: green">R</span><span style="color: orange">345</span><span style="color: pink">F</span><span style="color: orange">2</span><span style="color: red">LL</span>'
        test.assert_equals(highlight(code), expected, message.format(code))
        print(f"Correct highlighting: {expected}\nYour highlighting:    {highlight(code)}")
        
        code = "F3RF5LF7"
        expected = '<span style="color: pink">F</span><span style="color: orange">3</span><span style="color: green">R</span><span style="color: pink">F</span><span style="color: orange">5</span><span style="color: red">L</span><span style="color: pink">F</span><span style="color: orange">7</span>'
        test.assert_equals(highlight(code), expected, message.format(code))
        print(f"Correct highlighting: {expected}\nYour highlighting:    {highlight(code)}")