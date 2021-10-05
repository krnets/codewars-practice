#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing solution_algorithm")
{
	SUBCASE("should_handle_basic_test_cases")
	{
		CHECK(solution(10) == 23);
	}
}
