#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Max_adjacent_Product")
{
	SUBCASE("Positive__Numbers")
	{
		CHECK(adjacentElementsProduct({5, 8}) == 40);
		CHECK(adjacentElementsProduct({1, 2, 3}) == 6);
		CHECK(adjacentElementsProduct({1, 5, 10, 9}) == 90);
		CHECK(adjacentElementsProduct({5, 1, 2, 3, 1, 4}) == 6);
		CHECK(adjacentElementsProduct({4, 12, 3, 1, 5}) == 48);
	}
	SUBCASE("MiXed_Values")
	{
		CHECK(adjacentElementsProduct({3, 6, -2, -5, 7, 3}) == 21);
		CHECK(adjacentElementsProduct({9, 5, 10, 2, 24, -1, -48}) == 50);
		CHECK(adjacentElementsProduct({5, 6, -4, 2, 3, 2, -23}) == 30);
		CHECK(adjacentElementsProduct({-23, 4, -5, 99, -27, 329, -2, 7, -921}) == -14);
	}
	SUBCASE("Containg_Zeroes")
	{
		CHECK(adjacentElementsProduct({1, 0, 1, 0, 1000}) == 0);
		CHECK(adjacentElementsProduct({1, 2, 3, 0}) == 6);
	}
}
