#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SquaresNeeded")
{
	SUBCASE("BasicTests")
	{
		CHECK(squaresNeeded(0) == 0);
		CHECK(squaresNeeded(1) == 1);
		CHECK(squaresNeeded(2) == 2);
		CHECK(squaresNeeded(3) == 2);
		CHECK(squaresNeeded(4) == 3);
		CHECK(squaresNeeded(5) == 3);
		CHECK(squaresNeeded(6) == 3);
		CHECK(squaresNeeded(7) == 3);
		CHECK(squaresNeeded(8) == 4);
		CHECK(squaresNeeded(9) == 4);
		CHECK(squaresNeeded(10) == 4);
		CHECK(squaresNeeded(11) == 4);
		CHECK(squaresNeeded(12) == 4);
		CHECK(squaresNeeded(20) == 5);
		CHECK(squaresNeeded(30) == 5);
		CHECK(squaresNeeded(40) == 6);
		CHECK(squaresNeeded(50) == 6);
		CHECK(squaresNeeded(60) == 6);
		CHECK(squaresNeeded(64) == 7);
	}
}
