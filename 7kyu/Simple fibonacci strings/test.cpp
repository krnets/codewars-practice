#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_Fibonacci_Strings")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve(0) == "0");
		CHECK(solve(1) == "01");
		CHECK(solve(2) == "010");
		CHECK(solve(3) == "01001");
		CHECK(solve(5) == "0100101001001");
	}
}
