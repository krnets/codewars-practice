#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Kata")
{
	SUBCASE("Fixed_tests")
	{
		CHECK(solution(0) == "Value is 00000");
		CHECK(solution(5) == "Value is 00005");
		CHECK(solution(109) == "Value is 00109");
		CHECK(solution(1204) == "Value is 01204");
	}
}
