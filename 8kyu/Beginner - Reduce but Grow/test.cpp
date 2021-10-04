#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ReduceGrow)")
{
	using vec = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(grow(vec{1, 2, 3}) == 6);
		CHECK(grow(vec{4, 1, 1, 1, 4}) == 16);
		CHECK(grow(vec{2, 2, 2, 2, 2, 2}) == 64);
	}
}
