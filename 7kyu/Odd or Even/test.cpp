#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void do_test(const std::vector<int>& arr, const std::string& expected)
{
	CHECK(odd_or_even(arr) == expected);
}

TEST_CASE("testing odd_or_even")
{
	SUBCASE("edge_tests")
	{
		do_test({0}, "even");
		do_test({1}, "odd");
		do_test({}, "even");
	}
	SUBCASE("even_tests")
	{
		do_test({0, 1, 5}, "even");
		do_test({0, 1, 3}, "even");
		do_test({1023, 1, 2}, "even");
	}
	SUBCASE("negative_even_tests")
	{
		do_test({0, -1, -5}, "even");
		do_test({0, -1, -3}, "even");
		do_test({-1023, 1, -2}, "even");
	}
	SUBCASE("odd_tests")
	{
		do_test({0, 1, 2}, "odd");
		do_test({0, 1, 4}, "odd");
		do_test({1023, 1, 3}, "odd");
	}
	SUBCASE("negative_odd_tests")
	{
		do_test({0, -1, 2}, "odd");
		do_test({0, 1, -4}, "odd");
		do_test({-1023, -1, 3}, "odd");
	}
}
