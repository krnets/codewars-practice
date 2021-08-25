#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing seriesSum")
{
	SUBCASE("ExampleTests")
	{
		CHECK(seriesSum(0) == "0.00");
		CHECK(seriesSum(9) == "1.77");
		CHECK(seriesSum(15) == "1.94");
		CHECK(seriesSum(39) == "2.26");
		CHECK(seriesSum(58) == "2.40");
	}
}
