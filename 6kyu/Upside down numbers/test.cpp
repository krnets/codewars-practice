#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Upside_down_numbers")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve(0, 1000) == 19);
		CHECK(solve(1000, 10000) == 20);
		CHECK(solve(60000, 70000) == 15);
		CHECK(solve(60000, 130000) == 55);
	}
}
