#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Multiplication_Table")
{
	using VVI = vector<vector<int>>;

	SUBCASE("BasicTests 3")
	{
		CHECK(multiplication_table(3) == VVI{{1, 2, 3}, {2, 4, 6}, {3, 6, 9}});
	}
	SUBCASE("BasicTests 5")
	{
		CHECK(multiplication_table(5) == VVI{ {{1, 2, 3, 4, 5}, {2, 4, 6, 8, 10}, {3, 6, 9, 12, 15}, {4, 8, 12, 16, 20},
		      {5, 10, 15, 20, 25}} });
	}
}
