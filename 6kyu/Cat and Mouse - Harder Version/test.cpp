#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing CatMouse")
{
	SUBCASE("BasicTests")
	{
		CHECK(catMouse("..D.....Cm", 13) == "Caught!");
		CHECK(catMouse("............C.............D..m...", 8) == "Escaped!");
		CHECK(catMouse("m.C...", 5) == "boring without all three");
		CHECK(catMouse(".CD......m.", 10) == "Protected!");
		CHECK(catMouse("..D.....C.m", 2) == "Caught!");
	}
}
