#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Sample_tests")
{
	SUBCASE("Valid_positive_values")
	{
		CHECK(is_digit("35.65") == true);
		CHECK(is_digit("365") == true);
	}
	SUBCASE("Valid_negative_values")
	{
		CHECK(is_digit("-234.4") == true);
		CHECK(is_digit("-0") == true);
	}
	SUBCASE("Null")
	{
		CHECK(is_digit("0.0") == true);
	}
	SUBCASE("Invalid_cases")
	{
		CHECK(is_digit("s2324") == false);
		CHECK(is_digit("3 4") == false);
		CHECK(is_digit("3-4") == false);
		CHECK(is_digit("3 4   ") == false);
		CHECK(is_digit("") == false);
		CHECK(is_digit(" ") == false);
	}
}
