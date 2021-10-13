#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(unsigned long long ans, unsigned long long sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing sumFracts_Tests")
{
	SUBCASE("test1")
	{
		testequal(Finance::finance(5), 105);
		testequal(Finance::finance(6), 168);
		testequal(Finance::finance(8), 360);
		testequal(Finance::finance(15), 2040);
	}
}
