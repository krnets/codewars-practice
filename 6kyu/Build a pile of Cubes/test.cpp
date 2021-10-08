#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(long long ans, long long sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing findNb_Tests")
{
	SUBCASE("test1")
	{
		testequal(ASum::findNb(4183059834009), 2022);
		testequal(ASum::findNb(24723578342962), -1);
		testequal(ASum::findNb(135440716410000), 4824);
		testequal(ASum::findNb(40539911473216), 3568);
		testequal(ASum::findNb(26825883955641), 3218);
	}
}
