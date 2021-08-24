#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

void testequal(int ans, int sol)
{
	CHECK(ans == sol);
}

void dotest(int p0, double percent, int aug, int p, int expected)
{
	testequal(Arge::nbYear(p0, percent, aug, p), expected);
}

TEST_CASE("testing nbYear_Tests")
{
	SUBCASE("Fixed__Tests")
	{
		dotest(1500, 5, 100, 5000, 15);
		dotest(1500000, 2.5, 10000, 2000000, 10);
		dotest(1500000, 0.25, 1000, 2000000, 94);
		dotest(1500000, 0.25, -1000, 2000000, 151);
	}
}
