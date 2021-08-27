#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sequenceSum")
{
	SUBCASE("ExampleTests")
	{
		CHECK(sequenceSum(2, 6, 2) == 12);
		CHECK(sequenceSum(1, 5, 1) == 15);
		CHECK(sequenceSum(1, 5, 3) == 5);
		CHECK(sequenceSum(0, 15, 3) == 45);
		CHECK(sequenceSum(16, 15, 3) == 0);
		CHECK(sequenceSum(2, 24, 22) == 26);
		CHECK(sequenceSum(2, 2, 2) == 2);
		CHECK(sequenceSum(2, 2, 1) == 2);
		CHECK(sequenceSum(1, 15, 3) == 35);
		CHECK(sequenceSum(15, 1, 3) == 0);
	}
}
