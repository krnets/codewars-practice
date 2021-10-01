#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_Square_numbers")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve(8, 2) == make_pair(2, 6));
		CHECK(solve(10, 3) == make_pair(-1, -1));
		CHECK(solve(12, 4) == make_pair(4, 8));
		CHECK(solve(12, 5) == make_pair(-1, -1));
		CHECK(solve(50, 10) == make_pair(10, 40));
		CHECK(solve(50, 4) == make_pair(-1, -1));
		CHECK(solve(10, 5) == make_pair(5, 5));
		CHECK(solve(100, 5) == make_pair(5, 95));
		CHECK(solve(1000, 5) == make_pair(5, 995));
	}
}
