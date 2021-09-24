#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing basic_tests")
{
	SUBCASE("should_find_missing_numbers")
	{
		CHECK(findDeletedNumber({1,2,3,4,5,6,7,8,9},{5,7,1,9,4,8,2,3}) == 6);
		CHECK(findDeletedNumber({1},{}) == 1);
	}
	SUBCASE("should_respond_to_no_missing_numbers")
	{
		CHECK(findDeletedNumber({1,2,3,4,5,6,7},{2,3,6,1,5,4,7}) == 0);
		CHECK(findDeletedNumber({1,2,3,4,5,6,7,8,9},{5,7,6,9,4,8,1,2,3}) == 0);
	}
	SUBCASE("should_respond_to_nil_array")
	{
		CHECK(findDeletedNumber({},{}) == 0);
	}
}
