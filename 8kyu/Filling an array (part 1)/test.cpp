#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <vector>

TEST_CASE("testing Example_Tests")
{
	using V = std::vector<int>;

	SUBCASE("example_tests")
	{
		CHECK(arr() == V {});
		CHECK(arr(4) == V{0, 1, 2, 3});
	}
}
