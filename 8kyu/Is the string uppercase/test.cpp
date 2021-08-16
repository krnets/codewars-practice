#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Is_UpperCase")
{
	SUBCASE("Basic_Tests")
	{
		CHECK(is_uppercase("c") == false);
		CHECK(is_uppercase("C") == true);
		CHECK(is_uppercase("hello I AM DONALD") == false);
		CHECK(is_uppercase("HELLO I AM DONALD") == true);
		CHECK(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == false);
		CHECK(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == true);
	}
}
