#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("should_pass_all_the_tests_provided")
	{
		CHECK(circleOfNumbers(10, 2) == 7);
		CHECK(circleOfNumbers(4, 1) == 3);
		CHECK(circleOfNumbers(6, 3) == 0);
		CHECK(circleOfNumbers(10, 7) == 2);
	}
}
