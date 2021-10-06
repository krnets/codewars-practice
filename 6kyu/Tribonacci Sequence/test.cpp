#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Basic_tests")
{
	SUBCASE("Test_1")
	{
		std::vector<int> signature = {1, 1, 1};
		std::vector<int> expected = {1, 1, 1, 3, 5, 9, 17, 31, 57, 105};
		CHECK(tribonacci(signature, 10) == expected);
	}

	SUBCASE("Test_2")
	{
		std::vector<int> signature = {0, 0, 1};
		std::vector<int> expected = {0, 0, 1, 1, 2, 4, 7, 13, 24, 44};
		CHECK(tribonacci(signature, 10) == expected);
	}

	SUBCASE("Test_3")
	{
		std::vector<int> signature = {0, 1, 1};
		std::vector<int> expected = {0, 1, 1, 2, 4, 7, 13, 24, 44, 81};
		CHECK(tribonacci(signature, 10) == expected);
	}

	SUBCASE("Test_4")
	{
		std::vector<int> signature = {1, 0, 0};
		std::vector<int> expected = {1, 0, 0, 1, 1, 2, 4, 7, 13, 24};
		CHECK(tribonacci(signature, 10) == expected);
	}

	SUBCASE("Test_5")
	{
		std::vector<int> signature = {1, 2, 3};
		std::vector<int> expected = {1, 2, 3, 6, 11, 20, 37, 68, 125, 230};
		CHECK(tribonacci(signature, 10) == expected);
	}

	SUBCASE("Test_6")
	{
		std::vector<int> signature = {1, 2, 3};
		std::vector<int> expected = {1, 2};
		CHECK(tribonacci(signature, 2) == expected);
	}

	SUBCASE("Test_7")
	{
		int third = rand() % 10;
		std::vector<int> signature = {1, 2, third};
		std::vector<int> expected = {};
		CHECK(tribonacci(signature, 0) == expected);
	}
}
