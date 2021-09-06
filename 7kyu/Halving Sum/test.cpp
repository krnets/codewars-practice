#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing halving_sum")
{
	SUBCASE("Sample_Tests")
	{
		CHECK(halving_sum(25) == 47);
		CHECK(halving_sum(127) == 247);
	}
}
