#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sum_Two_Intgers")
{
	SUBCASE("Check_Positive_Values")
	{
		CHECK(Add(1, 2) == 3);
		CHECK(Add(5, 19) == 24);
		CHECK(Add(23, 17) == 40);
	}
	SUBCASE("Check_Negative_Values")
	{
		CHECK(Add(-14, -16) == -30);
		CHECK(Add(-50, -176) == -226);
		CHECK(Add(-10, -29) == -39);
	}
	SUBCASE("Check_Mixture_Values")
	{
		CHECK(Add(-13, 13) == 0);
		CHECK(Add(-27, 18) == -9);
		CHECK(Add(-90, 30) == -60);
	}
}
