#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Check_Three_Elements_Vector")
{
	SUBCASE("Return_Maximum_Product")
	{
		CHECK(maxProduct({4, 3, 5}, 2) == 20);
		CHECK(maxProduct({10, 8, 7, 9}, 3) == 720);
		CHECK(maxProduct({8, 6, 4, 6}, 3) == 288);
	}
	SUBCASE("Checks_Larger_Vector_Size")
	{
		CHECK(maxProduct({10, 2, 3, 8, 1, 10, 4}, 5) == 9600);
		CHECK(maxProduct({13, 12, -27, -302, 25, 37, 133, 155, -14}, 5) == 247895375);
	}
	SUBCASE("Checks_Negative_Values")
	{
		CHECK(maxProduct({-4, -27, -15, -6, -1}, 2) == 4);
		CHECK(maxProduct({-17, -8, -102, -309}, 2) == 136);
	}
	SUBCASE("Checks_Mixture_Values")
	{
		CHECK(maxProduct({10, 3, -27, -1}, 3) == -30);
		CHECK(maxProduct({14, 29, -28, 39, -16, -48}, 4) == -253344);
	}
}
