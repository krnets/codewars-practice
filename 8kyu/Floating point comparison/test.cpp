#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing approx_equals")
{
	SUBCASE("sample tests")
	{
		CHECK(approx_equals(175.9827, 82.25) == false);
		CHECK(approx_equals(-156.24037, -156.24038) == true);
		CHECK(approx_equals(123.2345, 123.234501) == true);
		CHECK(approx_equals(1456.3652, 1456.3641) == false);
		CHECK(approx_equals(-1.234, -1.233999) == true);
		CHECK(approx_equals(98.7655, 98.7654999) == true);
		CHECK(approx_equals(-7.28495, -7.28596) == false);
	}
}
