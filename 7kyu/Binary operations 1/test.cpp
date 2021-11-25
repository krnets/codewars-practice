#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Binary operations #1")
{
	SUBCASE("Basic_cases")
	{
		CHECK(flip_bit(0, 16) == 32768);
		CHECK(flip_bit(565, 6) == 533);
		CHECK(flip_bit(127, 8) == 255);
	}
}
