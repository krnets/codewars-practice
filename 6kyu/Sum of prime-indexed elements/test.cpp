#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sum_of_prime_indexed_elements")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve(std::vector<int>{}) == 0);
		CHECK(solve(std::vector<int>{1, 2, 3, 4}) == 7);
		CHECK(solve(std::vector<int>{1, 2, 3, 4, 5, 6}) == 13);
		CHECK(solve(std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}) == 47);
	}
}
