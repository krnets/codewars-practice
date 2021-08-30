#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing factorial")
{
	SUBCASE("Sample_Tests")
	{
		CHECK(factorial(0) == 1);
		CHECK(factorial(1) == 1);
		CHECK(factorial(2) == 2);
		CHECK(factorial(3) == 6);
		CHECK(factorial(4) == 24);
		CHECK(factorial(5) == 120);
		CHECK(factorial(6) == 720);
		CHECK(factorial(7) == 5040);
	}
}
