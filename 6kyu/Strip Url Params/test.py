import codewars_test as test
from kata import strip_url_params


url1 = 'www.codewars.com?a=1&b=2'
url2 = 'www.codewars.com?a=1&b=2&a=1&b=3'
url3 = 'www.codewars.com?a=1'
url4 = 'www.codewars.com'

test.assert_equals(strip_url_params(url1), url1, "Didn't return correct value when given a url that had nothing to be stripped")
test.assert_equals(strip_url_params(url2), url1, "Didn't strip duplicates from url")
test.assert_equals(strip_url_params(url2, ['b']), url3, "Didn't strip param that was specified in paramsToStrip array")
test.assert_equals(strip_url_params(url4, ['b']), url4, "Didn't return an un-modifed url when there was nothing to strip")
test.assert_equals(strip_url_params(url1, ['a', 'b']), url4, "Didn't strip all parameters")