#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Sample_Test_Cases")
{
	SUBCASE("Fixed_Tests")
	{
		CHECK(integrate(3,2) == "1x^3");
		CHECK(integrate(12,5) == "2x^6");
		CHECK(integrate(20,1) == "10x^2");
		CHECK(integrate(40,3) == "10x^4");
		CHECK(integrate(90,2) == "30x^3");
	}
}
