#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Clock")
{
	SUBCASE("BasicTests")
	{
		CHECK(past(0, 1, 1) == 61000);
		CHECK(past(1, 1, 1) == 3661000);
		CHECK(past(0, 0, 0) == 0);
		CHECK(past(1, 0, 1) == 3601000);
		CHECK(past(1, 0, 0) == 3600000);
	}
}
