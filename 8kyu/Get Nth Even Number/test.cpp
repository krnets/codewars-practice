#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing NthEven")
{
	SUBCASE("FixedTests")
	{
		CHECK(nthEven(1) == 0);
		CHECK(nthEven(2) == 2);
		CHECK(nthEven(3) == 4);
		CHECK(nthEven(6) == 10);
		CHECK(nthEven(101) == 200);
		CHECK(nthEven(201) == 400);
		CHECK(nthEven(1001) == 2000);
	}
}
