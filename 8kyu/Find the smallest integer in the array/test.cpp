#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing findSmallest number")
{
	SUBCASE("check positive values")
	{
		CHECK(findSmallest({3,5,2}) == 2);
		CHECK(findSmallest({7,4,6,8}) == 4);
		CHECK(findSmallest({17,21,15,36,96}) == 15);
		CHECK(findSmallest({3,9,13,10,5,3,9,5}) == 3);
	}
	SUBCASE("check negative values")
	{
		CHECK(findSmallest({-12,-52,-27}) == -52);
		CHECK(findSmallest({-3,-27,-4,-2,-27,-2}) == -27);
		CHECK(findSmallest({-16,-37,-8,-46,-29}) == -46);
		CHECK(findSmallest({-14,-102,-96,-36,-46,-15,-44}) == -102);
	}
	SUBCASE("check mixed values")
	{
		CHECK(findSmallest({-12,0,-27}) == -27);
		CHECK(findSmallest({-13,-50,57,13,67,-13,57,108,67}) == -50);
		CHECK(findSmallest({-23,12,0,-47,-3,24}) == -47);
	}
}
