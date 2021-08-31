#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing CookingTime")
{
	SUBCASE("BasicTests")
	{
		CHECK(cookingTime(0) == 0);
		CHECK(cookingTime(1) == 5);
		CHECK(cookingTime(5) == 5);
		CHECK(cookingTime(8) == 5);
		CHECK(cookingTime(9) == 10);
		CHECK(cookingTime(10) == 10);
		CHECK(cookingTime(16) == 10);
		CHECK(cookingTime(20) == 15);
		CHECK(cookingTime(100) == 65);
		CHECK(cookingTime(1000) == 625);
	}
}
