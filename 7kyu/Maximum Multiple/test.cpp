#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Maximum_Multiple")
{
	SUBCASE("Check_Small_Positives")
	{
		CHECK(maxMultiple(2, 7) == 6);
		CHECK(maxMultiple(3, 10) == 9);
		CHECK(maxMultiple(7, 17) == 14);
	}
	SUBCASE("Larger_Positives")
	{
		CHECK(maxMultiple(10, 50) == 50);
		CHECK(maxMultiple(37, 200) == 185);
		CHECK(maxMultiple(7, 100) == 98);
	}
}
