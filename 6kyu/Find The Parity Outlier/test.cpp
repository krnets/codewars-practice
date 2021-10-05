#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Parity Outlier")
{
	SUBCASE("Simple_Tests")
	{
		CHECK(FindOutlier({2, 3, 4}) == 3);
		CHECK(FindOutlier({1, 2, 3}) == 2);
		CHECK(FindOutlier({4, 1, 3, 5, 9}) == 4);
	}
}
