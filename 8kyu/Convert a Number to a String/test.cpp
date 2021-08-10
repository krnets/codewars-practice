#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing number to string")
{
	SUBCASE("should_convert_a_number_to_string")
	{
		CHECK(number_to_string(1+2) == "3");
		CHECK(number_to_string(67) == "67");
		CHECK(number_to_string(-5) == "-5");
	}
}
