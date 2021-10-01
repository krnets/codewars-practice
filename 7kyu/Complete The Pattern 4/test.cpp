#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("BasicTest1")
	{
		std::string expected = "1";

		std::string actual = pattern(1);

		CHECK(("\n" + actual) == ("\n" + expected));
	}

	SUBCASE("BasicTest2")
	{
		std::string expected =
			"12\n"
			"2";

		std::string actual = pattern(2);

		CHECK(("\n" + actual) == ("\n" + expected));
	}

	SUBCASE("BasicTest_5")
	{
		std::string expected =
			"12345\n"
			"2345\n"
			"345\n"
			"45\n"
			"5";

		std::string actual = pattern(5);

		CHECK(("\n" + actual) == ("\n" + expected));
	}

	SUBCASE("BasicTest_11")
	{
		std::string expected =
			"1234567891011\n"
			"234567891011\n"
			"34567891011\n"
			"4567891011\n"
			"567891011\n"
			"67891011\n"
			"7891011\n"
			"891011\n"
			"91011\n"
			"1011\n"
			"11";

		std::string actual = pattern(11);

		CHECK(("\n" + actual) == ("\n" + expected));
	}
}
