#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sortByLength")
{
	Kata kata;
	using V = std::vector<std::string>;

	SUBCASE("ExampleTest1")
	{
		CHECK(kata.sortByLength({"Beg", "Life", "I", "To"}) == V{"I", "To", "Beg", "Life"});
	}

	SUBCASE("ExampleTest2")
	{
		CHECK(kata.sortByLength({"", "Moderately", "Brains", "Pizza"}) == V{"", "Pizza", "Brains", "Moderately"});
	}

	SUBCASE("ExampleTest3")
	{
		CHECK(kata.sortByLength({"Longer", "Longest", "Short"}) == V{"Short", "Longer", "Longest"});
	}
}
