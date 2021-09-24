#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Basic_Values")
{
	using vec = std::vector<int>;

	SUBCASE("Check_Positive_Values")
	{
		CHECK(nthSmallest(vec{3, 1, 2}, 2) == 2);
		CHECK(nthSmallest(vec{15, 20, 7, 10, 4, 3}, 3) == 7);
	}
	SUBCASE("Check_Negative_Values")
	{
		CHECK(nthSmallest(vec{-5, -1, -6, -18}, 4) == -1);
		CHECK(nthSmallest(vec{-102, -16, -1, -2, -367, -9}, 5) == -2);
	}
	SUBCASE("Check_Mixed_Values")
	{
		CHECK(nthSmallest(vec{2, 169, 13, -5, 0, -1}, 4) == 2);
		CHECK(nthSmallest(vec{177, 225, 243, -169, -12, -5, 2, 92}, 5) == 92);
	}
}
