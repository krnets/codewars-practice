#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Next_Happy_Year")
{
	SUBCASE("Check_Basic_Values")
	{
		CHECK(nextHappyYear(1001) == 1023);
		CHECK(nextHappyYear(1123) == 1203);
		CHECK(nextHappyYear(2001) == 2013);
		CHECK(nextHappyYear(2334) == 2340);
		CHECK(nextHappyYear(3331) == 3401);
		CHECK(nextHappyYear(2342) == 2345);
		CHECK(nextHappyYear(1987) == 2013);
		CHECK(nextHappyYear(2013) == 2014);
		CHECK(nextHappyYear(3000) == 3012);
	}
	SUBCASE("Check_Larger_Values")
	{
		CHECK(nextHappyYear(5555) == 5601);
		CHECK(nextHappyYear(7712) == 7801);
		CHECK(nextHappyYear(8088) == 8091);
		CHECK(nextHappyYear(8800) == 8901);
		CHECK(nextHappyYear(8989) == 9012);
		CHECK(nextHappyYear(8977) == 9012);
		CHECK(nextHappyYear(6869) == 6870);
		CHECK(nextHappyYear(8999) == 9012);
	}
}
