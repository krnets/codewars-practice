#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing SampleTests")
{
	SUBCASE("should_pass_sample_tests")
	{
		CHECK(sum_str("4", "5") == "9");
		CHECK(sum_str("34", "5") == "39");
		CHECK(sum_str("42", "") == "42");
		CHECK(sum_str("", "42") == "42");
	}
}
