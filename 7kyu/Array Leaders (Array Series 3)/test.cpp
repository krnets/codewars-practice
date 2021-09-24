#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Array_Leaders")
{
	using vec = vector<int>;
	SUBCASE("Check_Positive_Values")
	{
		CHECK(arrayLeaders(vec{1, 2, 3, 4, 0}) == vec{4});
		CHECK(arrayLeaders(vec{16, 17, 4, 3, 5, 2}) == vec{17, 5, 2});
	}
	SUBCASE("Check_Negativee_Values")
	{
		CHECK(arrayLeaders(vec{-1, -29, -26, -2}) == vec{-1});
		CHECK(arrayLeaders(vec{-36, -12, -27}) == vec{-36, -12});
	}
	SUBCASE("Mixed_Values")
	{
		CHECK(arrayLeaders(vec{5, 2}) == vec{5, 2});
		CHECK(arrayLeaders(vec{0, -1, -29, 3, 2}) == vec{0, -1, 3, 2});
	}
}
