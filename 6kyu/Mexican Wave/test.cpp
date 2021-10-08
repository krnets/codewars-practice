#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Wave_tests")
{
	using V = vector<string>;

	SUBCASE("test 1")
	{
		CHECK(wave("hello") == V{
		      "Hello",
		      "hEllo",
		      "heLlo",
		      "helLo",
		      "hellO"});
	}
	SUBCASE("test 2")
	{
		CHECK(wave("codewars") == V{
		      "Codewars",
		      "cOdewars",
		      "coDewars",
		      "codEwars",
		      "codeWars",
		      "codewArs",
		      "codewaRs",
		      "codewarS" });
	}
	SUBCASE("test 3")
	{
		CHECK(wave("") == V{});
	}
	SUBCASE("test 4")
	{
		CHECK(wave("two words") == V{
		      "Two words",
		      "tWo words",
		      "twO words",
		      "two Words",
		      "two wOrds",
		      "two woRds",
		      "two worDs",
		      "two wordS" });
	}
	SUBCASE("test 5")
	{
		CHECK(wave(" gap ") == V{
		      " Gap ",
		      " gAp ",
		      " gaP "});
	}
}
