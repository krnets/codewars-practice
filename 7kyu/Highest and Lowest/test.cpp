#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing HighAndLow")
{
	SUBCASE("BasicTests")
	{
		CHECK(highAndLow("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214");
		CHECK(highAndLow("10 2 -2 -10") == "10 -10");
		CHECK(highAndLow("1 -1") == "1 -1");
		CHECK(highAndLow("1 1") == "1 1");
		CHECK(highAndLow("-1 -1") == "-1 -1");
		CHECK(highAndLow("1 -1 0") == "1 -1");
		CHECK(highAndLow("1 1 0") == "1 0");
		CHECK(highAndLow("-1 -1 0") == "0 -1");
		CHECK(highAndLow("42") == "42 42");
	}
}
