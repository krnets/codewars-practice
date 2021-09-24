#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Jumping_Number")
{
	SUBCASE("Single_Digit_Number")
	{
		CHECK(jumpingNumber(9) == "Jumping!!");
		CHECK(jumpingNumber(1) == "Jumping!!");
		CHECK(jumpingNumber(7) == "Jumping!!");
	}
	SUBCASE("Two_Digit_Number")
	{
		CHECK(jumpingNumber(23) == "Jumping!!");
		CHECK(jumpingNumber(32) == "Jumping!!");
		CHECK(jumpingNumber(79) == "Not!!");
		CHECK(jumpingNumber(98) == "Jumping!!");
	}
	SUBCASE("Larger_Numbers")
	{
		CHECK(jumpingNumber(8987) == "Jumping!!");
		CHECK(jumpingNumber(4343456) == "Jumping!!");
		CHECK(jumpingNumber(98789876) == "Jumping!!");
	}
}
