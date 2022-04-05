#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(long long ans, long long sol)
{
	CHECK(ans == sol);
}

void dotest(long long n, long long expected)
{
	testequal(MaxRotate::maxRot(n), expected);
}

TEST_CASE("testing maxRot_Tests")
{
	SUBCASE("Fixed__Tests")
	{
		dotest(38458215, 85821534);
		dotest(195881031, 988103115);
		dotest(896219342, 962193428);
		dotest(69418307, 94183076);
	}
}
