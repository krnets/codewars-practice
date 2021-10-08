#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Kata")
{
	SUBCASE("Example_Test_Cases 1")
	{
		CHECK(queueTime({}, 1) == 0);
		CHECK(queueTime({1, 2, 3, 4}, 1) == 10);
		CHECK(queueTime({2, 2, 3, 3, 4, 4}, 2) == 9);
		CHECK(queueTime({1, 2, 3, 4, 5}, 100) == 5);
	}
	SUBCASE("Example_Test_Cases 2")
	{
		CHECK(queueTime({5, 3, 4}, 1) == 12);
		CHECK(queueTime({10, 2, 3, 3}, 2) == 10);
		CHECK(queueTime({2, 3, 10}, 2) == 12);
	}
}
