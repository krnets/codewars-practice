#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing basic_tests")
{
	SUBCASE("it_should_work_for_basic_tests")
	{
		CHECK(deleteDigit(152) == 52);
		CHECK(deleteDigit(1001) == 101);
		CHECK(deleteDigit(10) == 1);
	}
}
