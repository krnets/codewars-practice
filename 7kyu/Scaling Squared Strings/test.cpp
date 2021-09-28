#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void testequal(string ans, string sol)
{
	CHECK(ans == sol);
}

TEST_CASE("testing ")
{
	SUBCASE("Fixed_Tests_scale")
	{
		string d = "abcd\nefgh\nijkl\nmnop";
		string s =
			"aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp";

		testequal(ScalingSqStrings::scale(d, 2, 3), s);
		testequal(ScalingSqStrings::scale("", 5, 5), "");
		testequal(ScalingSqStrings::scale("Kj\nSH", 1, 2), "Kj\nKj\nSH\nSH");
	}
}
