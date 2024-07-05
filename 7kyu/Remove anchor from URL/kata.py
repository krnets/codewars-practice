import codewars_test as test


# def remove_url_anchor(url):
#     pos = url.find("#")
#     return url[:pos] if pos >= 0 else url


# def remove_url_anchor(url):
#     return url.split("#")[0]

from urllib import parse


def remove_url_anchor(url):
    return parse.urldefrag(url)[0]


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            remove_url_anchor("www.codewars.com#about"), "www.codewars.com"
        )
        test.assert_equals(
            remove_url_anchor("www.codewars.com/katas/?page=1#about"),
            "www.codewars.com/katas/?page=1",
        )
        test.assert_equals(
            remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/"
        )
