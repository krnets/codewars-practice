#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <vector>

TEST_CASE("testing SummingArrays")
{
	using vec = std::vector<int>;

	SUBCASE("FixedTests")
	{
		CHECK(sum(vec{}) == 0);
		CHECK(sum(vec{5}) == 5);
		CHECK(sum(vec{-5}) == -5);
		CHECK(sum(vec{1, 2, 3, 4}) == 10);
		CHECK(sum(vec{1, 2, -3, 3, 4}) == 7);
	}
}
