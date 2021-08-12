#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing abbrevName")
{
	SUBCASE("Fixed_tests")
	{
		CHECK(abbrevName("Sam Harris") == "S.H");
		CHECK(abbrevName("Patrick Feenan") == "P.F");
		CHECK(abbrevName("Evan Cole") == "E.C");
		CHECK(abbrevName("P Favuzzi") == "P.F");
		CHECK(abbrevName("David Mendieta") == "D.M");
		CHECK(abbrevName("george clooney") == "G.C");
		CHECK(abbrevName("marky mark") == "M.M");
		CHECK(abbrevName("eliza doolittle") == "E.D");
		CHECK(abbrevName("reese witherspoon") == "R.W");
	}
}
