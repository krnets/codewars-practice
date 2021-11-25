#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing FirstNSmallest")
{
	using V = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(firstNSmallest(V{1, 2, 3, 4, 5}, 3) == V{1, 2, 3});
		CHECK(firstNSmallest(V{5, 4, 3, 2, 1}, 3) == V{3, 2, 1});
		CHECK(firstNSmallest(V{1, 2, 3, 1, 2}, 3) == V{1, 2, 1});
		CHECK(firstNSmallest(V{1, 2, 3, -4, 0}, 3) == V{1, -4, 0});
		CHECK(firstNSmallest(V{1, 2, 3, 4, 5}, 0) == V{});
		CHECK(firstNSmallest(V{1, 2, 3, 4, 5}, 5) == V{1, 2, 3, 4, 5});
		CHECK(firstNSmallest(V{1, 2, 3, 4, 2}, 4) == V{1, 2, 3, 2});
		CHECK(firstNSmallest(V{2, 1, 2, 3, 4, 2}, 2) == V{2, 1});
		CHECK(firstNSmallest(V{2, 1, 2, 3, 4, 2}, 3) == V{2, 1, 2});
		CHECK(firstNSmallest(V{2, 1, 2, 3, 4, 2}, 4) == V{2, 1, 2, 2});
	}
}
