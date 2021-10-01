#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing consecutive")
{
	SUBCASE("Test_Cases")
	{
		CHECK(consecutive({1, 2, 3, 4, 5, 6, 7, 8, 9}, 2, 8) == false);
		CHECK(consecutive({1, 2, 3, 4, 5, 6, 7, 8, 9}, 2, 3) == true);
		CHECK(consecutive({1, 4, 5, 3, 2, 7, 6, 23, 76, 11, 0}, 2, 3) == true);
		CHECK(consecutive({1, -4, -5, 3, -2, 11, 23, -76, 6, -7, 2}, 2, 3) == false);
		CHECK(consecutive({1, 2, 3, 4, 5}, 1, 5) == false);
		CHECK(consecutive({1, 2, 3, 4, 5}, 5, 1) == false);
	}
}
