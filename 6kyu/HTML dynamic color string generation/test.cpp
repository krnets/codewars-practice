#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing GenerateColorRGBTest")
{
	SUBCASE("symbolTest")
	{
		std::string actual = GenerateColorRGB::generateColor(std::rand() % 0x1000001);
		CHECK(actual.substr(0, 1) == "#");
		CHECK(actual.length() >= 4);
		CHECK(actual.length() <= 7);
	}
}
