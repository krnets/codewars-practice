#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Arithmophobia")
{
	SUBCASE("Example_Tests")
	{
		CHECK(am_i_afraid("Monday", 13) == false);
		CHECK(am_i_afraid("Sunday", -666) == true);
		CHECK(am_i_afraid("Tuesday", 2) == false);
		CHECK(am_i_afraid("Tuesday", 965) == true);
		CHECK(am_i_afraid("Friday", 2) == true);
	}
}
