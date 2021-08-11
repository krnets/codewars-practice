#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Century_From_The_Year")
{
	SUBCASE("Extract_The_Century_From_Given_Year")
	{
		CHECK(centuryFromYear(1705) == 18);
		CHECK(centuryFromYear(1900) == 19);
		CHECK(centuryFromYear(1601) == 17);
		CHECK(centuryFromYear(2000) == 20);
	}
}
