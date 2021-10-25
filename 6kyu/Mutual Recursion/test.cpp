#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_tests")
{
	SUBCASE("should_pass_all_tests_for_F")
	{
		CHECK(1 == F(0));
		CHECK(3 == F(5));
		CHECK(6 == F(10));
		CHECK(9 == F(15));
		CHECK(16 == F(25));
	}

	SUBCASE("should_pass_all_tests_for_M")
	{
		CHECK(0 == M(0));
		CHECK(3 == M(5));
		CHECK(6 == M(10));
		CHECK(9 == M(15));
		CHECK(16 == M(25));
	}
}
