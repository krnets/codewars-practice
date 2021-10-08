#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

using std::vector;

void testequal(vector<int> ans, vector<int> sol)
{
	CHECK(ans == sol);
}

void dotest(int v1, int v2, int g, vector<int> expected)
{
	testequal(Tortoise::race(v1, v2, g), expected);
}

TEST_CASE("testing race_Tests")
{
	SUBCASE("Fixed__Tests")
	{
		dotest(720, 850, 70, {0, 32, 18});
		dotest(820, 81, 550, {-1, -1, -1});
		dotest(80, 91, 37, {3, 21, 49});
	}
}
