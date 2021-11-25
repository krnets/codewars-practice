#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple reversal game")
{
	SUBCASE("Sample_Tests")
	{
		CHECK(solve(4,1) == 3);
		CHECK(solve(4,2) == 2);
		CHECK(solve(4,3) == 0);
		CHECK(solve(20,8) == 17);
		CHECK(solve(20,9) == 19);
		CHECK(solve(20,10) == 18);
	}
}
