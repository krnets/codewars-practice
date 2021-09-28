#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Max_min_arrays")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve(std::vector<int>{15, 11, 10, 7, 12}) == std::vector<int>{15, 7, 12, 10, 11});
		CHECK(solve(std::vector<int>{84, 79, 76, 61, 78}) == std::vector<int>{84, 61, 79, 76, 78});
		CHECK(solve(std::vector<int>{1, 6, 9, 4, 3, 7, 8, 2}) == std::vector<int>{9, 1, 8, 2, 7, 3, 6, 4});
	}
}
