#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing divisible_by")
{
	using V = std::vector<int>;

	SUBCASE("example tests")
	{
		CHECK(divisible_by({1, 2, 3, 4, 5, 6}, 2) == V{2, 4, 6});
		CHECK(divisible_by({1, 2, 3, 4, 5, 6}, 3) == V{3, 6});
		CHECK(divisible_by({0, 1, 2, 3, 4, 5, 6}, 4) == V{0, 4});
		CHECK(divisible_by({0}, 4) == V{0});
		CHECK(divisible_by({1, 3, 5}, 2) == V{});
		CHECK(divisible_by({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 1) == V{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
	}
}
