#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing Sample_Tests")
{
	SUBCASE("Tests")
	{
		CHECK(twice_as_old(36, 7) == 22);
		CHECK(twice_as_old(55, 30) == 5);
		CHECK(twice_as_old(42, 21) == 0);
		CHECK(twice_as_old(22, 1) == 20);
		CHECK(twice_as_old(29, 0) == 29);
	}
}
