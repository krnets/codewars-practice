#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Maximum_Triplet_Sum")
{
	SUBCASE("Check_Positive_Values")
	{
		CHECK(maxTriSum({3, 2, 6, 8, 2, 3}) == 17);
		CHECK(maxTriSum({2, 9, 13, 10, 5, 2, 9, 5}) == 32);
		CHECK(maxTriSum({2, 1, 8, 0, 6, 4, 8, 6, 2, 4}) == 18);
	}
	SUBCASE("Check_Negative_Values")
	{
		CHECK(maxTriSum({-3, -27, -4, -2, -27, -2}) == -9);
		CHECK(maxTriSum({-14, -12, -7, -42, -809, -14, -12}) == -33);
	}
	SUBCASE("Check_Mixture_Values")
	{
		CHECK(maxTriSum({-13, -50, 57, 13, 67, -13, 57, 108, 67}) == 232);
		CHECK(maxTriSum({-7, 12, -7, 29, -5, 0, -7, 0, 0, 29}) == 41);
	}
}
