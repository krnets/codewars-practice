#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing seven")
{
	using P = std::pair<long long, long long>;

	SUBCASE("Fixed_Tests")
	{
		CHECK(DivSeven::seven(371) == P{35, 1});
		CHECK(DivSeven::seven(1603) == P{7, 2});
		CHECK(DivSeven::seven(1021) == P{10, 2});
		CHECK(DivSeven::seven(477557101) == P{28, 7});
		CHECK(DivSeven::seven(477557102) == P{47, 7});
		CHECK(DivSeven::seven(234002979) == P{21, 7});
	}
}
