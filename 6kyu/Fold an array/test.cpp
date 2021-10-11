#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	Kata kata;

	SUBCASE("ExampleTest1")
	{
		std::vector<int> expected = {6, 6, 3};
		std::vector<int> actual = kata.foldArray({1, 2, 3, 4, 5}, 1);
		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest2")
	{
		std::vector<int> expected = {9, 6};
		std::vector<int> actual = kata.foldArray({1, 2, 3, 4, 5}, 2);
		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest3")
	{
		std::vector<int> expected = {15};
		std::vector<int> actual = kata.foldArray({1, 2, 3, 4, 5}, 3);
		CHECK(actual == expected);
	}

	SUBCASE("ExampleTest4")
	{
		std::vector<int> expected = {14, 75, 0};
		std::vector<int> actual = kata.foldArray({-9, 9, -8, 8, 66, 23}, 1);
		CHECK(actual == expected);
	}
}
