#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Center of the Matrix")
{
	SUBCASE("SampleTest 1")
	{
		CHECK(center({ { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } }) == 5);
	}
	SUBCASE("SampleTest 2")
	{
		CHECK(center({{1, 2, 3}, {4, 5, 6}}) == std::nullopt);
	}
}
