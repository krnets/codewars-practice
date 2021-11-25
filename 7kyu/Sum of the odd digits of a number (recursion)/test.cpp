#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sum of the odd digits of a number (recursion)")
{
	SUBCASE("basic_tests")
	{
		CHECK(sum_odd_digits(258) == 5);
		CHECK(sum_odd_digits(234) == 3);
		CHECK(sum_odd_digits(0) == 0);
	}
}
