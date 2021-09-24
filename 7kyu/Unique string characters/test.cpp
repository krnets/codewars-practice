#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Unique_String_Characters")
{
	SUBCASE("Example_tests")
	{
		CHECK(solve("xyab", "xzca") == "ybzc");
		CHECK(solve("xyabb", "xzca") == "ybbzc");
		CHECK(solve("abcd", "xyz") == "abcdxyz");
		CHECK(solve("xxx", "xzca") == "zca");
	}
}
