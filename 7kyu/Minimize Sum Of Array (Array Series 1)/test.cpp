#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing minSum")
{
	SUBCASE("return_minmum_Sum_Of_Numbers")
	{
		CHECK(minSum({5, 4, 2, 3}) == 22);
		CHECK(minSum({12, 6, 10, 26, 3, 24}) == 342);
		CHECK(minSum({9, 2, 8, 7, 5, 4, 0, 6}) == 74);
	}
}
