#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing stringToNumber")
{
	SUBCASE("shouldWorkForTheExamples")
	{
		CHECK(string_to_number("123456") == 123456);
		CHECK(string_to_number("352605") == 352605);
		CHECK(string_to_number("-321405") == -321405);
		CHECK(string_to_number("-7") == -7);
		CHECK(string_to_number("0") == 0);
		CHECK(string_to_number("-0") == 0);
	}
}
