#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"
#include <vector>

TEST_CASE("testing Example_Tests")
{
	using V = vector<int>;

	SUBCASE("example_tests")
	{
		CHECK(arr() == V {});
		CHECK(arr(4) == V{0, 1, 2, 3});
	}
}
