#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing simple_tests")
{
	SUBCASE("should_pass_all_simple_tests")
	{
		CHECK(bmi(81.585, 2.1) == "Underweight");
		CHECK(bmi(90.25, 1.9) == "Normal");
		CHECK(bmi(86.7, 1.7) == "Overweight");
		CHECK(bmi(200, 1.6) == "Obese");
	}
}
