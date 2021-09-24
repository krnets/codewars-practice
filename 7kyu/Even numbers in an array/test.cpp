#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing EvenNumbers")
{
	using V = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(evenNumbers(V{1, 2, 3, 4, 5, 6, 7, 8, 9}, 3) == V{4, 6, 8});
		CHECK(evenNumbers(V{-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26}, 2) == V{-8, 26});
		CHECK(evenNumbers(V{6, -25, 3, 7, 5, 5, 7, -3, 23}, 1) == V{6});
		CHECK(evenNumbers(V{1, 2, 3, 4, 5, 6, 7, 8, 9}, 4) == V{2, 4, 6, 8});
		CHECK(evenNumbers(V{1, 3, 5, 7, 9}, 0) == V{});
	}
}
