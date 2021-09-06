#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("basicTests")
	{
		CHECK(growingPlant(100, 10, 910) == 10);
		CHECK(growingPlant(10, 9, 4) == 1);
	}
}
