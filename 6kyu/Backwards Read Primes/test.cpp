#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("")
	{
		CHECK(BackWardsPrime::backwardsPrime(7000, 7100) == "7027 7043 7057");
		CHECK(BackWardsPrime::backwardsPrime(70000, 70245) == "70001 70009 70061 70079 70121 70141 70163 70241");
	}
}
