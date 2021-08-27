#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing nbDig")
{
	SUBCASE("Fixed_Tests")
	{
		CHECK(CountDig::nbDig(10, 1) == 4);
		CHECK(CountDig::nbDig(5750, 0) == 4700);
		CHECK(CountDig::nbDig(11011, 2) == 9481);
		CHECK(CountDig::nbDig(12224, 8)== 7733);
	}
}
