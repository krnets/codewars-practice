#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fixed_tests")
{
	SUBCASE("Digital_root")
	{
		CHECK(digital_root(16) == 7);
		CHECK(digital_root(195) == 6);
		CHECK(digital_root(992) == 2);
		CHECK(digital_root(167346) == 9);
		CHECK(digital_root(0) == 0);
	}
}
