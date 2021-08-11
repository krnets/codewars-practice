#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing square sum")
{
	SUBCASE("should_pass_some_basic_tests")
	{
		CHECK(square_sum({1, 2}) == 5);
		CHECK(square_sum({0, 3, 4, 5}) == 50);
		CHECK(square_sum({}) == 0);
		CHECK(square_sum({-1, -2}) == 5);
		CHECK(square_sum({-1, 0, 1}) == 2);
	}
}
