#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sortMyString")
{
	SUBCASE("Static_Ones")
	{
		CHECK(sortMyString("CodeWars") == "CdWr oeas");
		CHECK(sortMyString("YCOLUE'VREER") == "YOU'RE CLEVER");
	}
}
