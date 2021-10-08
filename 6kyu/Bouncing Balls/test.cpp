#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(int ans, int sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing bouncingBall_Tests")
{
	SUBCASE("test1")
	{
		testequal(Bouncingball::bouncingBall(3, 0.66, 1.5), 3);
		testequal(Bouncingball::bouncingBall(30, 0.66, 1.5), 15);
	}
}
