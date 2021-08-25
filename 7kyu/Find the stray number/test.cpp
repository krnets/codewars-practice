#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing stray")
{
	SUBCASE("simple_array_1")
	{
		CHECK(stray({ 1, 1, 2 }) == 2);
		CHECK(stray({ 1, 2, 2 }) == 1);
		CHECK(stray({ 17, 17, 3, 17, 17, 17, 17 }) == 3);
		CHECK(stray({ 8, 1, 1, 1, 1, 1, 1 }) == 8);
	}
}
