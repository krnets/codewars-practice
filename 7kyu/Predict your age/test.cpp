#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing predictAge")
{
	SUBCASE("Example_tests")
	{
		CHECK(predictAge(65, 60, 75, 55, 60, 63, 64, 45) == 86);
		CHECK(predictAge(32,54,76,65,34,63,64,45) == 79);
	}
}
