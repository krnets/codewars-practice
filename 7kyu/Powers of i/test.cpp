#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing basic_tests")
{
	SUBCASE("powers_0_through_10")
	{
		CHECK(pofi(0) == "1");
		CHECK(pofi(1) == "i");
		CHECK(pofi(2) == "-1");
		CHECK(pofi(3) == "-i");
		CHECK(pofi(4) == "1");
		CHECK(pofi(5) == "i");
		CHECK(pofi(6) == "-1");
		CHECK(pofi(7) == "-i");
		CHECK(pofi(8) == "1");
		CHECK(pofi(9) == "i");
		CHECK(pofi(10) == "-1");
	}
}
