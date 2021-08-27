#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing declareWinner")
{
	SUBCASE("BasicTest1")
	{
		Fighter fighter1("Lew", 10, 2);
		Fighter fighter2("Harry", 5, 4);

		std::string expected = "Lew";
		std::string actual = declareWinner(&fighter1, &fighter2, "Lew");

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest2")
	{
		Fighter fighter1("Lew", 10, 2);
		Fighter fighter2("Harry", 5, 4);

		std::string expected = "Harry";
		std::string actual = declareWinner(&fighter1, &fighter2, "Harry");

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest3")
	{
		Fighter fighter1("Harald", 20, 5);
		Fighter fighter2("Harry", 5, 4);

		std::string expected = "Harald";
		std::string actual = declareWinner(&fighter1, &fighter2, "Harry");

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest4")
	{
		Fighter fighter1("Harald", 20, 5);
		Fighter fighter2("Harry", 5, 4);

		std::string expected = "Harald";
		std::string actual = declareWinner(&fighter1, &fighter2, "Harald");

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest5")
	{
		Fighter fighter1("Jerry", 30, 3);
		Fighter fighter2("Harald", 20, 5);

		std::string expected = "Harald";
		std::string actual = declareWinner(&fighter1, &fighter2, "Jerry");

		CHECK(actual == expected);
	}

	SUBCASE("BasicTest6")
	{
		Fighter fighter1("Jerry", 30, 3);
		Fighter fighter2("Harald", 20, 5);

		std::string expected = "Harald";
		std::string actual = declareWinner(&fighter1, &fighter2, "Harald");

		CHECK(actual == expected);
	}
}
