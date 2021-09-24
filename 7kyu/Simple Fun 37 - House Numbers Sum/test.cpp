#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void doTest(const std::vector<int>& arr, int expected)
{
	CHECK(house_numbers_sum(arr) == expected);
}

TEST_CASE("testing sample_test")
{
	SUBCASE("basic_tests")
	{
		doTest({5, 1, 2, 3, 0, 1, 5, 0, 2}, 11);
		doTest({4, 2, 1, 6, 0}, 13);
		doTest({4, 1, 2, 3, 0, 10, 2}, 10);
		doTest({0, 1, 2, 3, 4, 5}, 0);
	}
}
