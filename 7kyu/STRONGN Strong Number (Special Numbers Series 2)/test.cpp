#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing strong_number")
{
	SUBCASE("assert_basic_tests")
	{
		CHECK(strong_num(1) == "STRONG!!!!");
		CHECK(strong_num(2) == "STRONG!!!!");
		CHECK(strong_num(145) == "STRONG!!!!");
	}
	SUBCASE("assert_basic_tests_2")
	{
		CHECK(strong_num(7) == "Not Strong !!");
		CHECK(strong_num(93) == "Not Strong !!");
		CHECK(strong_num(185) == "Not Strong !!");
	}
}
