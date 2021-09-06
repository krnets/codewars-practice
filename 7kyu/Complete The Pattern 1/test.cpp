#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing pattern")
{
	SUBCASE("ExampleTests")
	{
		std::string expected = "1\n22";
		std::string actual = pattern(2);
		CHECK("\n" + actual == "\n" + expected);

		expected = "1\n22\n333";
		actual = pattern(3);
		CHECK("\n" + actual == "\n" + expected);

		expected = "1\n22\n333\n4444\n55555";
		actual = pattern(5);
		CHECK("\n" + actual == "\n" + expected);

		expected =
			"1\n22\n333\n4444\n55555\n666666\n7777777\n88888888\n999999999\n10101010101010101010\n1111111111111111111111";
		actual = pattern(11);
		CHECK("\n" + actual == "\n" + expected);
	}
}
