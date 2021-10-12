#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing twos_difference")
{
	using vpii = vector<std::pair<int, int>>;

	SUBCASE("sample tests")
	{
		CHECK(twos_difference({1, 2, 3, 4}) == vpii{{1, 3}, {2, 4}});
		CHECK(twos_difference({1, 3, 4, 6}) == vpii{{1, 3}, {4, 6}});
		CHECK(twos_difference({0, 3, 1, 4}) == vpii{{1, 3}});
		CHECK(twos_difference({4, 1, 2, 3}) == vpii{{1, 3}, {2, 4}});
		CHECK(twos_difference({6, 3, 4, 1, 5}) == vpii{{1, 3}, {3, 5}, {4, 6}});
		CHECK(twos_difference({3, 1, 6, 4}) == vpii{{1, 3}, {4, 6}});
		CHECK(twos_difference({1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56}) == vpii{{1, 3}, {3, 5}, {6, 8}, {8, 10}, {10, 12}, {12, 14}});
		CHECK(twos_difference({1, 4, 7, 10}) == vpii{});
		CHECK(twos_difference({}) == vpii{});
	}
}
