#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"


void testequal(string ans, string sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing wallPaper")
{
	SUBCASE("example tests")
	{
		testequal(Wallpaper::wallPaper(6.3, 4.5, 3.29), "sixteen");
		testequal(Wallpaper::wallPaper(7.8, 2.9, 3.29), "sixteen");
		testequal(Wallpaper::wallPaper(6.3, 5.8, 3.13), "seventeen");
		testequal(Wallpaper::wallPaper(6.1, 6.7, 2.81), "sixteen");
		testequal(Wallpaper::wallPaper(4.0, 3.5, 3.0), "ten");
		testequal(Wallpaper::wallPaper(0.0, 3.5, 3.0), "zero");
	}
}
