#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing compare")
{
	SUBCASE("ExampleTests")
	{
		CHECK(compare("AD", "BC") == true);
		CHECK(compare("AD", "DD") == false);
		CHECK(compare("gf", "FG") == true);
		CHECK(compare("zz1", "") == true);
		CHECK(compare("ZzZz", "ffPFF") == true);
		CHECK(compare("kl", "lz") == false);
	}
}
