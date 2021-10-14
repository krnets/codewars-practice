#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Basic_Tests")
{
	SUBCASE("Test_1")
		{
		std::vector<int> signature = {0, 1};
		std::vector<int> expected = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34};
		CHECK(xbonacci(signature, 10) == expected);
	}
	SUBCASE("Test_2")
	{
		std::vector<int> signature = {1, 1};
		std::vector<int> expected = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};
		CHECK(xbonacci(signature, 10) == expected);
	}
	SUBCASE("Test_3")
	{
		std::vector<int> signature = {0, 0, 0, 0, 1};
		std::vector<int> expected = {0, 0, 0, 0, 1, 1, 2, 4, 8, 16};
		CHECK(xbonacci(signature, 10) == expected);
	}
	SUBCASE("Test_4")
	{
		std::vector<int> signature = {1, 0, 0, 0, 0, 0, 1};
		std::vector<int> expected = {1, 0, 0, 0, 0, 0, 1, 2, 3, 6};
		CHECK(xbonacci(signature, 10) == expected);
	}
	SUBCASE("Test_5")
	{
		std::vector<int> signature = {1, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		std::vector<int> expected = {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256};
		CHECK(xbonacci(signature, 20) == expected);
	}
	SUBCASE("Test_6")
	{
		std::vector<int> signature = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
		std::vector<int> expected = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		CHECK(xbonacci(signature, 9) == expected);
	}
	SUBCASE("Test_7")
	{
		std::vector<int> signature = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
		std::vector<int> expected = {};
		CHECK(xbonacci(signature, 0) == expected);
	}
	SUBCASE("Test_8")
	{
		std::vector<int> signature = {1, 1, 1, 1};
		std::vector<int> expected = {1, 1, 1, 1, 4, 7, 13, 25, 49, 94};
		CHECK(xbonacci(signature, 10) == expected);
	}
}
