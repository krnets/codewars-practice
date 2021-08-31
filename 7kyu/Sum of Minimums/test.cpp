#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Minimum_Sum")
{
	SUBCASE("Fixed_Tests")
	{
		std::vector<std::vector<int>> test = {{7, 9, 8, 6, 2}, {6, 3, 5, 4, 3}, {5, 8, 7, 4, 5}};
		CHECK(sum_of_minimums(test) == 9);

		test = {{11, 12, 14, 54}, {67, 89, 90, 56}, {7, 9, 4, 3}, {9, 8, 6, 7}};
		CHECK(sum_of_minimums(test) == 76);
	}
}
