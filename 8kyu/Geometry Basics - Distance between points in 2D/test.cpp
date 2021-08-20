#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing distance_between_two_points")
{
	SUBCASE("test_1")
	{
		CHECK(distance_between_two_points(Point{3, 3}, Point{3, 3}) == 0);
	}

	SUBCASE("test_2")
	{
		CHECK(distance_between_two_points(Point{5, 1}, Point{1, 4}) - 5 <= 0.000001);
	}
}
