#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing am_i_wilson")
{
	SUBCASE("should_return_false_for_composite_numbers")
	{
		CHECK(amIWilson(9) == false);
		CHECK(amIWilson(6) == false);
	}
	SUBCASE("should_return_false_for_nonwilson_primes")
	{
		CHECK(amIWilson(2) == false);
		CHECK(amIWilson(17) == false);
	}
	SUBCASE("should_return_true_for_wilson_primes")
	{
		CHECK(amIWilson(5) == true);
		CHECK(amIWilson(13) == true);
		CHECK(amIWilson(563) == true);
	}
}
