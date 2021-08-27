#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing TwoOldestAges")
{
	SUBCASE("ShouldSolveSimpleTests")
	{
		using V = std::vector<int>;
		CHECK(two_oldest_ages(V{1,5,87,45,8,8}) == V{45, 87});
		CHECK(two_oldest_ages(V{6,5,83,5,3,18}) == V{18, 83});
	}
}
