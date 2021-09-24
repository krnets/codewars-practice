#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Check_Less_than_Thousand")
{
	SUBCASE("check_Balanced_Number")
	{
		CHECK(balancedNum(7) == "Balanced");
		CHECK(balancedNum(959) == "Balanced");
		CHECK(balancedNum(13) == "Balanced");
		CHECK(balancedNum(432) == "Not Balanced");
		CHECK(balancedNum(424) == "Balanced");
	}
	SUBCASE("check_Larger_Number")
	{
		CHECK(balancedNum(1024) == "Not Balanced");
		CHECK(balancedNum(66545) == "Not Balanced");
		CHECK(balancedNum(295591) == "Not Balanced");
		CHECK(balancedNum(1230987) == "Not Balanced");
		CHECK(balancedNum(56239814) == "Balanced");
	}
}
