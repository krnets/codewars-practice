#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing FindOdd")
{
	using V = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(findOdd(V{20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5}) == 5);
		CHECK(findOdd(V{1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5}) == -1);
		CHECK(findOdd(V{20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5}) == 5);
		CHECK(findOdd(V{10}) == 10);
		CHECK(findOdd(V{1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1}) == 10);
	}
}
