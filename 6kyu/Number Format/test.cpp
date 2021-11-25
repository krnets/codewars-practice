#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing NumberFormat")
{
	SUBCASE("BasicTests")
	{
		CHECK(numberFormat(100000) == "100,000");
		CHECK(numberFormat(-420902) == "-420,902");
		CHECK(numberFormat(5678545) == "5,678,545");
		CHECK(numberFormat(3) == "3");
		CHECK(numberFormat(-3) == "-3");
	}
}
