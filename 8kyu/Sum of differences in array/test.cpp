#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Sample_Tests")
{
	SUBCASE("Fixed_Tests")
	{
		CHECK(sumOfDifferences({1, 2, 10}) == 9);
		CHECK(sumOfDifferences({-3, -2, -1}) == 2);
		CHECK(sumOfDifferences({1, 1, 1, 1}) == 0);
		CHECK(sumOfDifferences({-17, 17}) == 34);
		CHECK(sumOfDifferences({}) == 0);
		CHECK(sumOfDifferences({-1}) == 0);
		CHECK(sumOfDifferences({1}) == 0);
	}
}
