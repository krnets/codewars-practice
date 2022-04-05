#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Example_Test_Cases")
{
	SUBCASE("Test_1")
	{
		CHECK(pattern(1) == "1");
	}
	SUBCASE("Test_2")
	{
		CHECK(pattern(3) == "321\n32\n3");
	}
}
