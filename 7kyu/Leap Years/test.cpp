#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing IsLeapYear")
{
	SUBCASE("should_pass_all_the_tests_provided")
	{
		CHECK(IsLeapYear(1234) == false);
		CHECK(IsLeapYear(1984) == true);
		CHECK(IsLeapYear(1900) == false);
		CHECK(IsLeapYear(1200) == true);
		CHECK(IsLeapYear(1990) == false);
		CHECK(IsLeapYear(2000) == true);
		CHECK(IsLeapYear(2010) == false);
		CHECK(IsLeapYear(2013) == false);
	}
}
