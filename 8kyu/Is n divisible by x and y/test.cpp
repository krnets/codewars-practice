#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing IsDivisible")
{
	SUBCASE("BasicTests")
	{
		CHECK(isDivisible(3, 3, 4) == false);
		CHECK(isDivisible(12, 3, 4) == true);
		CHECK(isDivisible(8, 3, 4) == false);
		CHECK(isDivisible(48, 3, 4) == true);
		CHECK(isDivisible(100, 5, 10) == true);
		CHECK(isDivisible(100, 5, 3) == false);
		CHECK(isDivisible(4, 4, 2) == true);
		CHECK(isDivisible(5, 2, 3) == false);
		CHECK(isDivisible(17, 17, 17) == true);
		CHECK(isDivisible(17, 1, 17) == true);
	}
}
