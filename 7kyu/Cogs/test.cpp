#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Cogs")
{
	SUBCASE("example test")
	{
		CHECK(cog_rpm({100, 75}) == doctest::Approx(-4.0/3.0).epsilon( 0.001));
	}
}
