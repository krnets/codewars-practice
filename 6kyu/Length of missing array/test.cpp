#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("BasicTest1")
	{
		int expected = 3;

		vector<vector<int>> testInput = {{1, 2}, {4, 5, 1, 1}, {1}, {5, 6, 7, 8, 9}};
		int actual = getLengthOfMissingArray(testInput);

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest2")
	{
		int expected = 2;

		vector<vector<int>> testInput = {{5, 2, 9}, {4, 5, 1, 1}, {1}, {5, 6, 7, 8, 9}};
		int actual = getLengthOfMissingArray(testInput);

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest3")
	{
		int expected = 5;

		vector<vector<char>> testInput = {
			{'a', 'a', 'a'}, {'a', 'a'}, {'a', 'a', 'a', 'a'}, {'a'}, {'a', 'a', 'a', 'a', 'a', 'a'}
		};
		int actual = getLengthOfMissingArray(testInput);

		CHECK(actual == expected);
	}
}
