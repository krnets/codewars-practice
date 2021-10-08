#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sort the odd")
{
	SUBCASE("ExampleTest1")
	{
		std::vector<int> expected = {1, 3, 2, 8, 5, 4};

		Kata kata;
		std::vector<int> actual = kata.sortArray({5, 3, 2, 8, 1, 4});

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest2")
	{
		std::vector<int> expected = {1, 3, 5, 8, 0};

		Kata kata;
		std::vector<int> actual = kata.sortArray({5, 3, 1, 8, 0});

		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest3")
	{
		std::vector<int> expected = {};

		Kata kata;
		std::vector<int> actual = kata.sortArray({});

		CHECK(actual == expected);
	}
}
