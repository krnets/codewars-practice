#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void dotest(vector<string> arr, int k, string expected)
{
	CHECK(LongestConsec::longestConsec(arr, k) == expected);
}

TEST_CASE("testing longestConsec_Tests")
{
	SUBCASE("test 1")
	{
		vector<string> arr{"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"};
		dotest(arr, 2, "abigailtheta");
	}
	SUBCASE("test 2")
	{
		vector<string> arr{"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};
		dotest(arr, 1, "oocccffuucccjjjkkkjyyyeehh");
	}
	SUBCASE("test 3")
	{
		vector<string> arr{"tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"};
		dotest(arr, 2, "folingtrashy");
	}
	SUBCASE("test 4")
	{
		vector<string> arr{"it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"};
		dotest(arr, 3, "ixoyx3452zzzzzzzzzzzz");
	}
}
