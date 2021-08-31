#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing averages")
{
	SUBCASE("BasicTest1")
	{
		std::vector<double> expected = {2, 2, 2, 2};
		std::vector<double> actual = averages({2, 2, 2, 2, 2});

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest2")
	{
		std::vector<double> expected = {0, 0, 0, 0};
		std::vector<double> actual = averages({2, -2, 2, -2, 2});

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest3")
	{
		std::vector<double> expected = {2, 4, 3, -4.5};
		std::vector<double> actual = averages({1, 3, 5, 1, -10});

		CHECK(actual == expected);
	}
}
