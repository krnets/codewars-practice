#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_consecutive_pairs")
{
	SUBCASE("Example_tests")
	{
		using VI = std::vector<int>;
		CHECK(pairs(VI{1,2,5,8,-4,-3,7,6,5}) == 3);
		CHECK(pairs(VI{21, 20, 22, 40, 39, -56, 30, -55, 95, 94}) == 2);
		CHECK(pairs(VI{81, 44, 80, 26, 12, 27, -34, 37, -35}) == 0);
		CHECK(pairs(VI{-55, -56, -7, -6, 56, 55, 63, 62}) == 4);
		CHECK(pairs(VI{73, 72, 8, 9, 73, 72}) == 3);
	}
}
