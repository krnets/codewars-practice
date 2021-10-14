#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Minimum_Number")
{
	SUBCASE("check_Small_Array_Size")
	{
		CHECK(minimumNumber({3, 1, 2}) == 1);
		CHECK(minimumNumber({5, 2}) == 0);
		CHECK(minimumNumber({1, 1, 1}) == 0);
	}
	SUBCASE("check_Larger_Array_Size")
	{
		CHECK(minimumNumber({2, 12, 8, 4, 6}) == 5);
		CHECK(minimumNumber({50, 39, 49, 6, 17, 28}) == 2);
	}
}
