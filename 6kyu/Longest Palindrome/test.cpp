#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void doTest(const std::string& s, int expected, bool equals = true)
{
	if (equals)
		CHECK(longest_palindrome(s) == expected);
	else
		CHECK(longest_palindrome(s) != expected);
}

TEST_CASE("testing sample_test")
{
	SUBCASE("basic_tests")
	{
		doTest("", 0);
		doTest("a", 1);
		doTest("aa", 2);
		doTest("baa", 2);
		doTest("aab", 2);
		doTest("zyabyz", 6, false);
		doTest("baabcd", 4);
		doTest("baablkj12345432133d", 9);
		doTest("lolollolollolollolol", 20);
		doTest("abcdefghijklmnopqrstuvwxyz lolollolollolollolol", 20);
	}
}
