#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing CheckFactor")
{
	SUBCASE("ShouldReturnTrue")
	{
		CHECK(checkForFactor(10, 2) == true);
		CHECK(checkForFactor(63, 7) == true);
		CHECK(checkForFactor(2450, 5) == true);
		CHECK(checkForFactor(24612, 3) == true);
	}
	SUBCASE("ShouldReturnFalse")
	{
		CHECK(checkForFactor(9, 2) == false);
		CHECK(checkForFactor(653, 7) == false);
		CHECK(checkForFactor(2453, 5) == false);
		CHECK(checkForFactor(24617, 3) == false);
	}
}
