#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing LateRideTests")
{
	SUBCASE("BasicTests")
	{
		CHECK(lateRide(240) == 4);
		CHECK(lateRide(808) == 14);
		CHECK(lateRide(1439) == 19);
		CHECK(lateRide(0) == 0);
		CHECK(lateRide(23) == 5);
		CHECK(lateRide(8) == 8);
	}
}
