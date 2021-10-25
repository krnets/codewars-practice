#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(std::pair<int, int> ans, std::pair<int, int> sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing sumFracts_Tests")
{
	SUBCASE("test 1")
	{
		vector<vector<int>> a1 = {{1, 2}, {2, 9}, {3, 18}, {4, 24}, {6, 48}};
		testequal(SumFractions::sumFracts(a1), {85, 72});
	}
	SUBCASE("test 2")
	{
		vector<vector<int>> a2 = {{1, 2}, {1, 3}, {1, 4}};
		testequal(SumFractions::sumFracts(a2), {13, 12});
	}
	SUBCASE("test 3")
	{
		vector<vector<int>> a3 = {{1, 3}, {5, 3}};
		testequal(SumFractions::sumFracts(a3), {2, 1});
	}
	SUBCASE("test 4")
	{
		vector<vector<int>> a4 = {};
		testequal(SumFractions::sumFracts(a4), {0, 1});
	}
}
