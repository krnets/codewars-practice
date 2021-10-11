#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing basic")
{
	SUBCASE("example_tests")
	{
		CHECK(group_by_commas(1) == "1");
		CHECK(group_by_commas(12) == "12");
		CHECK(group_by_commas(123) == "123");
		CHECK(group_by_commas(1234) == "1,234");
		CHECK(group_by_commas(12345) == "12,345");
		CHECK(group_by_commas(123456) == "123,456");
		CHECK(group_by_commas(1234567) == "1,234,567");
		CHECK(group_by_commas(12345678) == "12,345,678");
		CHECK(group_by_commas(123456789) == "123,456,789");
		CHECK(group_by_commas(1234567890) == "1,234,567,890");
	}
	SUBCASE("edge cases")
	{
		CHECK(group_by_commas(0) == "0");
		CHECK(group_by_commas(326168038) == "326,168,038");
	}
}
