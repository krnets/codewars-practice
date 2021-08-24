#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing add_binary")
{
	SUBCASE("should_pass_sample_tests")
	{
		CHECK(add_binary(0, 0) == "0");
		CHECK(add_binary(0, 1) == "1");
		CHECK(add_binary(1, 0) == "1");
		CHECK(add_binary(1, 1) == "10");
		CHECK(add_binary(2, 2) == "100");
		CHECK(add_binary(5, 9) == "1110");
		CHECK(add_binary(10, 10) == "10100");
		CHECK(add_binary(51, 12) == "111111");
		CHECK(add_binary(100, 100) == "11001000");
		CHECK(add_binary(4096, 1) == "1000000000001");
		CHECK(add_binary(0, 2174483647) == "10000001100110111111110010111111");
	}
}
