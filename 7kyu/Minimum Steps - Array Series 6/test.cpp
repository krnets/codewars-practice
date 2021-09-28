#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Minimum_Steps")
{
	using vec = std::vector<int>;

	SUBCASE("Check_Small_Array_Size")
	{
		CHECK(minimumSteps((vec{4, 6, 3}), 7) == 1);
		CHECK(minimumSteps((vec{10, 9, 9, 8}), 17) == 1);
	}
	SUBCASE("Check_Larger_Array_Size")
	{
		CHECK(minimumSteps((vec{8, 9, 4, 2}), 23) == 3);
		CHECK(minimumSteps((vec{19, 98, 69, 28, 75, 45, 17, 98, 67}), 464) == 8);
	}
}
