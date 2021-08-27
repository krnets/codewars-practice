#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing number")
{
	SUBCASE("example tests")
	{
		using V = std::vector<std::string>;

		CHECK(number(V{}) == V{});
		CHECK(number(V{"a", "b", "c"}) == V{"1: a", "2: b", "3: c"});
	}
}
