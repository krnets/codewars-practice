#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Upturn Numeral Triangle")
{
	std::string expected, actual;

	SUBCASE("Testing 5")
	{
		expected = " 1 1 1 1 1\n  2 2 2 2\n   3 3 3\n    4 4\n     5";
		actual = pattern(5);
		CHECK_EQ("\n" + actual, "\n" + expected);
	}
	SUBCASE("Testing 7")
	{
		expected = " 1 1 1 1 1 1 1\n  2 2 2 2 2 2\n   3 3 3 3 3\n    4 4 4 4\n     5 5 5\n      6 6\n       7";
		actual = pattern(7);
		CHECK_EQ("\n" + actual, "\n" + expected);
	}
	SUBCASE("Testing 12")
	{
		expected =
			" 1 1 1 1 1 1 1 1 1 1 1 1\n  2 2 2 2 2 2 2 2 2 2 2\n   3 3 3 3 3 3 3 3 3 3\n    4 4 4 4 4 4 4 4 4\n     5 5 5 5 5 5 5 5\n      6 6 6 6 6 6 6\n       7 7 7 7 7 7\n        8 8 8 8 8\n         9 9 9 9\n          0 0 0\n           1 1\n            2";
		actual = pattern(12);
		CHECK_EQ("\n" + actual, "\n" + expected);
	}
	SUBCASE("Testing 21")
	{
		expected =
			" 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n   3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3\n    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4\n     5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5\n      6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6\n       7 7 7 7 7 7 7 7 7 7 7 7 7 7 7\n        8 8 8 8 8 8 8 8 8 8 8 8 8 8\n         9 9 9 9 9 9 9 9 9 9 9 9 9\n          0 0 0 0 0 0 0 0 0 0 0 0\n           1 1 1 1 1 1 1 1 1 1 1\n            2 2 2 2 2 2 2 2 2 2\n             3 3 3 3 3 3 3 3 3\n              4 4 4 4 4 4 4 4\n               5 5 5 5 5 5 5\n                6 6 6 6 6 6\n                 7 7 7 7 7\n                  8 8 8 8\n                   9 9 9\n                    0 0\n                     1";
		actual = pattern(21);
		CHECK_EQ("\n" + actual, "\n" + expected);
	}
}
