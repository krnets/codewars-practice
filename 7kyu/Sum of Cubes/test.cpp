#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sum of Cubes")
{
	SUBCASE("sample tests")
	{
		CHECK(sum_cubes(1) == 1);
		CHECK(sum_cubes(2) == 9);
		CHECK(sum_cubes(3) == 36);
		CHECK(sum_cubes(4) == 100);
		CHECK(sum_cubes(10) == 3025);
		CHECK(sum_cubes(123) == 58155876);
	}
}
