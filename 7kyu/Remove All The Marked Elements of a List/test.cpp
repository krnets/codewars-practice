#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing remove_values")
{
	std::vector<int> integers, values, expected;

	SUBCASE("sample test1")
	{
		integers = {1, 1, 2, 3, 1, 2, 3, 4};
		values = {1, 3};
		expected = {2, 2, 4};

		CHECK(remove_values(integers, values) == expected);
	}
	SUBCASE("sample test 2")
	{
		integers = {1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8};
		values = {1, 3, 4, 2};
		expected = {5, 6, 7, 8};

		CHECK(remove_values(integers, values) == expected);
	}
	SUBCASE("sample test 3")
	{
		integers = {8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3};
		values = {2, 4, 3};
		expected = {8, 7, 6, 5, 1};

		CHECK(remove_values(integers, values) == expected);
	}
}
