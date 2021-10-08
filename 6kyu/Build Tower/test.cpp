#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing towerBuilder")
{
	Kata kata;

	SUBCASE("ExampleTest1")
	{
		vector<string> expected = {"*"};
		vector<string> actual = kata.towerBuilder(1);
		CHECK(actual == expected);
	}
	SUBCASE("ExampleTest2")
	{
		vector<string> expected = {" * ", "***"};
		vector<string> actual = kata.towerBuilder(2);
		CHECK(actual == expected);
	}
	SUBCASE("ExampleTest3")
	{
		vector<string> expected = {"  *  ", " *** ", "*****"};
		vector<string> actual = kata.towerBuilder(3);
		CHECK(actual == expected);
	}
	SUBCASE("ExampleTest6")
	{
		vector<string> expected = {
			"     *     ",
			"    ***    ",
			"   *****   ",
			"  *******  ",
			" ********* ",
			"***********"
		};
		vector<string> actual = kata.towerBuilder(6);
		CHECK(actual == expected);
	}
}
