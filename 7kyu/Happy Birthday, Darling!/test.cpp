#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing womens_age")
{
	SUBCASE("Sample_Tests")
	{
		CHECK(womens_age(32) == "32? That's just 20, in base 16!");
		CHECK(womens_age(39) == "39? That's just 21, in base 19!");
	}
}
