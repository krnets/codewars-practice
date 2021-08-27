#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing isAscOrder")
{
	SUBCASE("0_BasicTests")
	{
		CHECK(isAscOrder({ 1, 2 }) == true);
		CHECK(isAscOrder({ 2, 1 }) == false);
		CHECK(isAscOrder({ 1, 2, 3 }) == true);
		CHECK(isAscOrder({ 1, 3, 2 }) == false);
		CHECK(isAscOrder({ 2, 1, 3 }) == false);
		CHECK(isAscOrder({ 2, 3, 1 }) == false);
		CHECK(isAscOrder({ 3, 1, 2 }) == false);
		CHECK(isAscOrder({ 3, 2, 1 }) == false);
	}

	SUBCASE("1_AdvancedTests")
	{
		CHECK(isAscOrder({ 1, 4, 13, 97, 508, 1047, 20058 }) == true);
		CHECK(isAscOrder({ 56, 98, 123, 67, 742, 1024, 32, 90969 }) == false);
	}
}
