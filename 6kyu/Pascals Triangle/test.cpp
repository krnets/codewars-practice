#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("Depth_1")
	{
		CHECK(pascalsTriangle(1) == std::vector<long long>{1});
	}
	SUBCASE("Depth_2")
	{
		CHECK(pascalsTriangle(2) == std::vector<long long>{1, 1, 1});
	}
	SUBCASE("Depth_4")
	{
		CHECK(pascalsTriangle(4) == std::vector<long long>{1, 1, 1, 1, 2, 1, 1, 3, 3, 1});
	}
}
