#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing boolean_to_string_method")
{
	SUBCASE("basic_tests")
	{
		CHECK(boolean_to_string(true) == "true");
		CHECK(boolean_to_string(false) == "false");
		CHECK(boolean_to_string(false) == "false");
		CHECK(boolean_to_string(true) == "true");
	}
}
