#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Invisible_Cubes")
{
	SUBCASE("notVisibleCubes")
	{
		CHECK(notVisibleCubes(1) == 0);
		CHECK(notVisibleCubes(2) == 0);
		CHECK(notVisibleCubes(3) == 1);
		CHECK(notVisibleCubes(5) == 27);
		CHECK(notVisibleCubes(1648392) == 4478988151721719000);
	}
}
