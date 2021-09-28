#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Recursion_101")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve(6,19) == std::make_pair(6,7));
		CHECK(solve(2,1) == std::make_pair(0,1));
		CHECK(solve(22,5) == std::make_pair(0,1));
		CHECK(solve(2,10) == std::make_pair(2,2));
		CHECK(solve(8796203,7556) == std::make_pair(1019,1442));
		CHECK(solve(19394,19394) == std::make_pair(19394,19394));
	}
}
