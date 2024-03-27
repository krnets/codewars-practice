from kata import Url_shortener
import codewars_test as test
import re

def test_format(string):
    return re.search("^short.ly\/[a-z]{1,4}$", string)

@test.describe("Should pass all of these")
def tests():
    @test.it("Testing two different URLs")
    def test_different():
        url_shortener = Url_shortener()
        short_url1 = url_shortener.shorten("https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e")
        test.expect(test_format(short_url1), message="Wrong format!")
        short_url2 = url_shortener.shorten("https://www.codewars.com/kata/5efae11e2d12df00331f91a6")
        test.expect(test_format(short_url2), message="Wrong format!")
        test.assert_equals(url_shortener.redirect(short_url1), "https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e")
        test.assert_equals(url_shortener.redirect(short_url2), "https://www.codewars.com/kata/5efae11e2d12df00331f91a6")
    
    @test.it("Testing same URLs")
    def test_same():
        url_shortener = Url_shortener()
        short_url1 = url_shortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
        test.expect(test_format(short_url1), message="Wrong format!")
        short_url2 = url_shortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
        test.expect(test_format(short_url2), message="Wrong format!")
        test.assert_equals(short_url1, short_url2, message="Should work with same long URLs")
        test.assert_equals(url_shortener.redirect(short_url1), "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")