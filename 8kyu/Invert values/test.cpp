#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing invert")
{
	SUBCASE("should_pass_some_basic_tests")
	{
		CHECK(invert({1, 2, 3, 4, 5}) == std::vector<int>{-1, -2, -3, -4, -5});
		CHECK(invert({1, -2, 3, -4, 5}) == std::vector<int>{-1, 2, -3, 4, -5});
		CHECK(invert({}) == std::vector<int>{});
	}
}
