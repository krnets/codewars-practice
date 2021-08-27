#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing dont_give_me_five_tests")
{
	SUBCASE("example_tests")
	{
		CHECK(dontGiveMeFive(1, 9) == 8);
		CHECK(dontGiveMeFive(4, 17) == 12);
		CHECK(dontGiveMeFive(1, 90) == 72);
		CHECK(dontGiveMeFive(-4, 17) == 20);
		CHECK(dontGiveMeFive(-4, 37) == 38);
		CHECK(dontGiveMeFive(-14, -1) == 13);
		CHECK(dontGiveMeFive(-14, -6) == 9);
	}
}
