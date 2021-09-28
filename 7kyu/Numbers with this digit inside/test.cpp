#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	std::vector<long> expected, actual;

	SUBCASE("Test1")
	{
		expected = {0, 0, 0};
		actual = numbersWithDigitInside(5, 6);
		CHECK(actual == expected);
	}
	SUBCASE("test2")
	{
		expected = {1, 6, 6};
		actual = numbersWithDigitInside(7, 6);
		CHECK(actual == expected);
	}
	SUBCASE("Test3")
	{
		expected = {3, 22, 110};
		actual = numbersWithDigitInside(11, 1);
		CHECK(actual == expected);
	}
	SUBCASE("Test4")
	{
		expected = {2, 30, 200};
		actual = numbersWithDigitInside(20, 0);
		CHECK(actual == expected);
	}
	SUBCASE("Test5")
	{
		expected = {9, 286, 5955146588160};
		actual = numbersWithDigitInside(44, 4);
		CHECK(actual == expected);
	}
}
