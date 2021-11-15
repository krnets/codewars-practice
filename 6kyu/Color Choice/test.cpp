#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void dotest(long long m, int n, long long expected)
{
	CHECK(ColorChoice::checkChoose(m, n) == expected);
}

TEST_CASE("testing Color Choice")
{
	SUBCASE("Fixed__Tests")
	{
		dotest(6, 4, 2);
		dotest(4, 4, 1);
		dotest(4, 2, -1);
		dotest(35, 7, 3);
	}
}
