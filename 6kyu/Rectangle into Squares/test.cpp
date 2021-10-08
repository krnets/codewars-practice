#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(std::vector<int> ans, std::vector<int> sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing sumFracts")
{
	SUBCASE("test1")
	{
		testequal(SqInRect::sqInRect(5, 5), {});
		testequal(SqInRect::sqInRect(5, 3), {3, 2, 1, 1});
	}
}
