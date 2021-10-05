#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing CountBits")
{
	SUBCASE("BasicTests")
	{
		CHECK(countBits(0) == 0);
		CHECK(countBits(4) == 1);
		CHECK(countBits(7) == 3);
		CHECK(countBits(9) == 2);
		CHECK(countBits(10) == 2);
		CHECK(countBits(26) == 3);
		CHECK(countBits(77231418) == 14);
		CHECK(countBits(12525589) == 11);
		CHECK(countBits(3811) == 8);
		CHECK(countBits(392902058) == 17);
	}
}
