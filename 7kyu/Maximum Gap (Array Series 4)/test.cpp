#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Maximum_Gap")
{
	SUBCASE("Check_Positive_Values")
	{
		CHECK(maxGap({13, 10, 2, 9, 5}) == 4);
		CHECK(maxGap({13, 3, 5}) == 8);
		CHECK(maxGap({24, 299, 131, 14, 26, 25}) == 168);
	}
	SUBCASE("Check_Negative_Values")
	{
		CHECK(maxGap({-3, -27, -4, -2}) == 23);
		CHECK(maxGap({-7, -42, -809, -14, -12}) == 767);
	}
	SUBCASE("Check_Mixed_Values")
	{
		CHECK(maxGap({12, -5, -7, 0, 290}) == 278);
		CHECK(maxGap({-54, 37, 0, 64, -15, 640, 0}) == 576);
	}
}
