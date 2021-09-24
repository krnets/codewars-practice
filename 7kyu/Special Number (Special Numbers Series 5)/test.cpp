#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Special_Number")
{
	SUBCASE("Check_Single_Digit_Number")
	{
		CHECK(specialNumber(2) == "Special!!");
		CHECK(specialNumber(3) == "Special!!");
		CHECK(specialNumber(9) == "NOT!!");
		CHECK(specialNumber(7) == "NOT!!");
	}
	SUBCASE("Two_Digit_Number")
	{
		CHECK(specialNumber(23) == "Special!!");
		CHECK(specialNumber(79) == "NOT!!");
		CHECK(specialNumber(32) == "Special!!");
		CHECK(specialNumber(39) == "NOT!!");
		CHECK(specialNumber(55) == "Special!!");
	}
	SUBCASE("Larger_Special_Number")
	{
		CHECK(specialNumber(513) == "Special!!");
		CHECK(specialNumber(709) == "NOT!!");
		CHECK(specialNumber(538) == "NOT!!");
	}
	SUBCASE("Mega_Sepcial_Number")
	{
		CHECK(specialNumber(53532) == "Special!!");
		CHECK(specialNumber(970569) == "NOT!!");
		CHECK(specialNumber(11350224) == "Special!!");
	}
}

