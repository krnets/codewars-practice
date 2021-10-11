#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing matrixAddition")
{
	vector<vector<int>> expected;

	SUBCASE("Sample_Test")
	{
		expected = {{3, 4, 4}, {6, 4, 4}, {2, 2, 4}};
		CHECK(matrixAddition({{1, 2, 3}, {3, 2, 1}, {1, 1, 1}}, {{2, 2, 1}, {3, 2, 3}, {1, 1, 3}}) == expected);

		expected = {{3}};
		CHECK(matrixAddition({{1}}, {{2}}) == expected);

		expected = {{3, 5}, {3, 5}};
		CHECK(matrixAddition({{1, 2}, {1, 2}}, {{2, 3}, {2, 3}}) == expected);
	}
}
