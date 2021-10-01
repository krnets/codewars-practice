#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(std::vector<int> ans, std::vector<int> sol)
{
	CHECK(ans == sol);
}

static void dotest(std::vector<int> arr, std::vector<int> expected)
{
	testequal(Valley::makeValley(arr), expected);
}

TEST_CASE("testing makeValley")
{
	SUBCASE("Fixed__Tests")
	{
		std::vector<int> d = {17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1};
		std::vector<int> sol = {17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17};
		dotest(d, sol);
		d = {20, 7, 6, 2};
		sol = {20, 6, 2, 7};
		dotest(d, sol);
		d = {};
		sol = {};
		dotest(d, sol);
		d = {14, 10, 8};
		sol = {14, 8, 10};
		dotest(d, sol);
	}
}
