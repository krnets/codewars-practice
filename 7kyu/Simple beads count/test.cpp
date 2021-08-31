#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("sample tests")
	{
		CHECK(countRedBeads(0) == 0);
		CHECK(countRedBeads(1) == 0);
		CHECK(countRedBeads(3) == 4);
		CHECK(countRedBeads(5) == 8);
	}
}
