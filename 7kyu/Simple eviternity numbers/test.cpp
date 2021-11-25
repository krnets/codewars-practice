#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_eviternity_numbers")
{
	SUBCASE("Example_tests")
	{
		CHECK_EQ(solve(0,100), 4);
		// 8, 58, 85, 88

		CHECK_EQ(solve(0,1000), 14);
		// 8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888

		CHECK_EQ(solve(0,10000), 37);
		CHECK_EQ(solve(0,100000), 103);
	}
}
