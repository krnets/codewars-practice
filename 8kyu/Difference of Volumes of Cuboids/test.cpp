#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <array>

TEST_CASE("testing DifferenceVolumesCuboids")
{
	using ar = std::array<int, 3>;

	SUBCASE("BasicTests")
	{
		CHECK(findDifference(ar{3, 2, 5}, ar{1, 4, 4}) == 14);
		CHECK(findDifference(ar{9, 7, 2}, ar{5, 2, 2}) == 106);
		CHECK(findDifference(ar{11, 2, 5}, ar{1, 10, 8}) == 30);
		CHECK(findDifference(ar{4, 4, 7}, ar{3, 9, 3}) == 31);
		CHECK(findDifference(ar{15, 20, 25}, ar{10, 30, 25}) == 0);
	}
}
