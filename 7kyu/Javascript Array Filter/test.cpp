#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing get_even_numbers")
{
	SUBCASE("Base_cases")
	{
		using V = std::vector<int>;
		CHECK(get_even_numbers(V{2, 4, 5, 6}) == V{2, 4, 6});
		CHECK(get_even_numbers(V{}) == V{});
		CHECK(get_even_numbers(V{1}) == V{});
		CHECK(get_even_numbers(V{1, 2}) == V{2});
		CHECK(get_even_numbers(V{1, 2, 3, 4, 5}) == V{2, 4});
		CHECK(get_even_numbers(V{2, 4, 6, 8}) == V{2, 4, 6, 8});
	}
}
