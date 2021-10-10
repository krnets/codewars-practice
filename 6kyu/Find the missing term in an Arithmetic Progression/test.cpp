#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing findMissing")
{
	SUBCASE("missing 7")
	{
		CHECK(findMissing({1, 3, 5, 9, 11}) == 7);
	}
	SUBCASE("missing 5")
	{
		CHECK(findMissing({1, 3, 7}) == 5);
	}
	SUBCASE("missing 3")
	{
		CHECK(findMissing({1, 5, 7}) == 3);
	}
	SUBCASE("missing 2002")
	{
		CHECK(findMissing({ 1001, 3003, 4004, 5005 }) == 2002);
	}
}
