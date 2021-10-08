#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing two_sum")
{
	using P = std::pair<size_t, size_t>;

	SUBCASE("example test")
	{
		CHECK(two_sum({1, 2, 3}, 4) == P{0, 2});
		CHECK(two_sum({1234, 5678, 9012}, 14690) == P{1, 2});
		CHECK(two_sum({2, 2, 3}, 4) == P{0, 1});
	}
}
