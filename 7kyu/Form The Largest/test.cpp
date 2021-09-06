#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing extracting_Max_from_digits")
{
	SUBCASE("pass_basic_tests")
	{
		CHECK(maxNumber(213) == 321);
		CHECK(maxNumber(7389) == 9873);
		CHECK(maxNumber(63792) == 97632);
	}
	SUBCASE("pass_digit_Occurrence_repeation")
	{
		CHECK(maxNumber(566797) == 977665);
		CHECK(maxNumber(2399783) == 9987332);
		CHECK(maxNumber(79797979) == 99997777);
	}
	SUBCASE("pass_large_numbers")
	{
		CHECK(maxNumber(17693284) == 98764321);
		CHECK(maxNumber(17758936) == 98776531);
		CHECK(maxNumber(134976658) == 987665431);
	}
}
