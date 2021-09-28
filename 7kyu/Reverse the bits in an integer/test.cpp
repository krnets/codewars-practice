#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fixed_tests")
{
	SUBCASE("Basic_cases")
	{
		CHECK(reverse_bits(417) == 267);
		CHECK(reverse_bits(267) == 417);
		CHECK(reverse_bits(0) == 0);
		CHECK(reverse_bits(2017) == 1087);
		CHECK(reverse_bits(1023) == 1023);
		CHECK(reverse_bits(1024) == 1);
	}
}
