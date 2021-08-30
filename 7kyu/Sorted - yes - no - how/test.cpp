#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing is_sorted_and_how_test")
{
	SUBCASE("simple_array_1")
	{
		CHECK(is_sorted_and_how({1, 2}) == "yes, ascending");
		CHECK(is_sorted_and_how({15, 7, 3, -8}) == "yes, descending");
		CHECK(is_sorted_and_how({4, 2, 30}) == "no");
	}
}
