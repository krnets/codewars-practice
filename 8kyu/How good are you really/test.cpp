#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <vector>

TEST_CASE("testing HowGoodAreYouReally")
{
	using vec = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(betterThanAverage(vec{2, 3}, 5) == true);
		CHECK(betterThanAverage(vec{100, 40, 34, 57, 29, 72, 57, 88}, 75) == true);
		CHECK(betterThanAverage(vec{12, 23, 34, 45, 56, 67, 78, 89, 90}, 69) == true);
	}
}
