#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Does array x contain all values within array y?")
{
	vector nums{1, 2, 3, 4, 5, 6, 7, 8, 9};

	SUBCASE("Valid_tests")
	{
		CHECK(contains_all(nums, {1, 2, 6}) == true);
		CHECK(contains_all(nums, {1}) == true);
		CHECK(contains_all(nums, {9}) == true);
		CHECK(contains_all(nums, {2, 4, 6, 8}) == true);
		CHECK(contains_all(nums, {1, 2, 3}) == true);
	}
	SUBCASE("Invalid_tests")
	{
		CHECK(contains_all(nums, {1, 15, 6}) == false);
		CHECK(contains_all(nums, {0}) == false);
		CHECK(contains_all(nums, {10}) == false);
		CHECK(contains_all(nums, {1, 5, 13}) == false);
	}
}
