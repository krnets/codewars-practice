#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fixed_tests")
{
	SUBCASE("Basic_cases")
	{
		CHECK(mygcd(1, 3) == 1);
		CHECK(mygcd(60, 12) == 12);
		CHECK(mygcd(2672, 5678) == 334);
	}
	SUBCASE("Larger_values")
	{
		CHECK(mygcd(10927782, 6902514) == 846);
		CHECK(mygcd(1590771464, 1590771620) == 4);
	}
}
