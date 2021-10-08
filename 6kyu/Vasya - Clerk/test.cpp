#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sample_Tests")
{
	SUBCASE("")
	{
		CHECK(tickets({25, 25, 50, 50}) == "YES");
		CHECK(tickets({25, 100}) == "NO");
	}
}
