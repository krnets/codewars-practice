#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing replace")
{
	SUBCASE("Basic_Tests")
	{
		CHECK(replace("Hi!") == "H!!");
		CHECK(replace("!Hi! Hi!") == "!H!! H!!");
		CHECK(replace("aeiou") == "!!!!!");
		CHECK(replace("ABCDE") == "!BCD!");
	}
}
