#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Basic_Test")
{
	SUBCASE("Disarium_Or_NOT")
	{
		CHECK(disariumNumber(89) == "Disarium !!");
		CHECK(disariumNumber(564) == "Not !!");
		CHECK(disariumNumber(1024) == "Not !!");
	}
	SUBCASE("Larger_numbers")
	{
		CHECK(disariumNumber(64599) == "Not !!");
		CHECK(disariumNumber(136586) == "Not !!");
		CHECK(disariumNumber(1048576) == "Not !!");
	}
}
