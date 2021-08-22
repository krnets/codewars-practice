#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing zero_fuel_function")
{
	SUBCASE("should_pass_sample_tests")
	{
		CHECK(zero_fuel(50, 25, 2) == true);
		CHECK(zero_fuel(100, 50, 1) == false);
	}
}
