#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing XO")
{
	SUBCASE("Sample_Test_Cases")
	{
		CHECK(XO("ooxx") == true);
		CHECK(XO("xooxx") == false);
		CHECK(XO("ooxXm") == true);
		CHECK(XO("zpzpzpp") == true);
		CHECK(XO("zzoo") == false);
	}
}
