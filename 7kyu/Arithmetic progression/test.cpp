#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing AritmeticSequenceElements")
{
	SUBCASE("BasicTests")
	{
		CHECK(arithmeticSequenceElements(1, 2, 5) == "1, 3, 5, 7, 9");
		CHECK(arithmeticSequenceElements(1, 0, 5) == "1, 1, 1, 1, 1");
		CHECK(arithmeticSequenceElements(1, -3, 10) == "1, -2, -5, -8, -11, -14, -17, -20, -23, -26");
		CHECK(arithmeticSequenceElements(100, -10, 10) == "100, 90, 80, 70, 60, 50, 40, 30, 20, 10");
	}
}
