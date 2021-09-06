#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ReverseNumber")
{
	SUBCASE("positive")
	{
		CHECK(reverseNumber(123) == 321);
		CHECK(reverseNumber(1000) == 1);
		CHECK(reverseNumber(4321234) == 4321234);
		CHECK(reverseNumber(5) == 5);
		CHECK(reverseNumber(0) == 0);
		CHECK(reverseNumber(98989898) == 89898989);
		CHECK(reverseNumber(1234567890) == 987654321);
		CHECK(reverseNumber(987654321) == 123456789);
	}
	SUBCASE("negative")
	{
		CHECK(reverseNumber(-123) == -321);
		CHECK(reverseNumber(-5) == -5);
		CHECK(reverseNumber(-9876543210) == -123456789);
	}
}
