#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Basics 08: Find next higher number with same Bits (1's)")
{
	SUBCASE("ExampleTest1")
	{
		CHECK(nextHigher(128) == 256);
	}
	SUBCASE("ExampleTest2")
	{
		CHECK(nextHigher(1) == 2);
	}
	SUBCASE("ExampleTest3")
	{
		CHECK(nextHigher(1022) == 1279);
	}
	SUBCASE("ExampleTest4")
	{
		CHECK(nextHigher(127) == 191);
	}
	SUBCASE("ExampleTest5")
	{
		CHECK(nextHigher(1253343) == 1253359);
	}
}
