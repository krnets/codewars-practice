#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_string_reversal")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve("codewars") == "srawedoc");
		CHECK(solve("your code") == "edoc ruoy");
		CHECK(solve("your code rocks") == "skco redo cruoy");
		CHECK(solve("our code") == "edo cruo");
	}
}
