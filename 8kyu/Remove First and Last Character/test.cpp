#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing ")
{
	SUBCASE("Check_Short_Length_String")
	{
		CHECK(sliceString("tuna") == "un");
		CHECK(sliceString("rats") == "at");
		CHECK(sliceString("code") == "od");
	}
	SUBCASE("Check_Longer_String")
	{
		CHECK(sliceString("country") == "ountr");
		CHECK(sliceString("place") == "lac");
		CHECK(sliceString("translation") == "ranslatio");
	}
}
