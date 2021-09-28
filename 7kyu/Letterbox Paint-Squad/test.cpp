#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Letterbox_Paint_Squad")
{
	SUBCASE("sample case")
	{
		CHECK(paint_letterboxes(125, 132) == std::array<int, 10>{1, 9, 6, 3, 0, 1, 1, 1, 1, 1});
	}
}
