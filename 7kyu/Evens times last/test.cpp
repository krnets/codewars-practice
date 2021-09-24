#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fixed_tests")
{
	SUBCASE("Basic_cases")
	{
		CHECK(even_last({2, 3, 4, 5}) == 30);
		CHECK(even_last({}) == 0);
		CHECK(even_last({2, 2, 2, 2}) == 8);
		CHECK(even_last({1, 3, 3, 1, 10}) == 140);
		CHECK(even_last({-11, 3, 3, 1, 10}) == 20);
		CHECK(even_last({-11}) == 121);
	}
}
