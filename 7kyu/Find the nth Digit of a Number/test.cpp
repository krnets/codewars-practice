#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing findDigit")
{
	SUBCASE("Examples")
	{
		CHECK(findDigit(5673, 4) == 5);
		CHECK(findDigit(129, 2) == 2);
		CHECK(findDigit(-2825, 3) == 8);
		CHECK(findDigit(-456, 4) == 0);
		CHECK(findDigit(0, 20) == 0);
		CHECK(findDigit(24, -8) == -1);
	}
}
