#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("should_pass_example_tests")
	{
		CHECK(to_time(3600) == "1 hour(s) and 0 minute(s)");
		CHECK(to_time(3500) == "0 hour(s) and 58 minute(s)");
		CHECK(to_time(323500) == "89 hour(s) and 51 minute(s)");
		CHECK(to_time(0) == "0 hour(s) and 0 minute(s)");
	}
}
