#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Cogs 2")
{
	SUBCASE("sample tests")
	{
		std::pair<double, double> actual = cog_rpm({100, 50, 25}, 1);

		CHECK(actual.first == doctest::Approx(-1.0 / 2.0).epsilon( 0.001));
		CHECK(actual.second == doctest::Approx(-2.0).epsilon( 0.001));
	}
}
