#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sum of positive number")
{
	SUBCASE("works_for_some_examples")
	{
		CHECK(positive_sum(std::vector <int> {1,2,3,4,5}) == 15);
		CHECK(positive_sum(std::vector <int> {1,-2,3,4,5}) == 13);
		CHECK(positive_sum(std::vector <int> {-1,2,3,4,-5}) == 9);
	}
	SUBCASE("returns_0_when_array_is_empty")
	{
		CHECK(positive_sum(std::vector <int> {}) ==0);
	}
	SUBCASE("returns_0_when_all_elements_are_negative")
	{
		CHECK(positive_sum(std::vector <int> {-1,-2,-3,-4,-5}) == 0);
	}
}
