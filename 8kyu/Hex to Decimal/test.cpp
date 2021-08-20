#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("BasicTests")
	{
		int expected = 1;
		int actual = hexToDec("1");
		CHECK(actual == expected);

		expected = 10;
		actual = hexToDec("a");
		CHECK(actual == expected);

		expected = 16;
		actual = hexToDec("10");
		CHECK(actual == expected);

		expected = 255;
		actual = hexToDec("FF");
		CHECK(actual == expected);

		expected = -12;
		actual = hexToDec("-C");
		CHECK(actual == expected);
	}
}
