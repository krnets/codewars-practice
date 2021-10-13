#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sequences_and_Series")
{
	SUBCASE("Sample_Test")
	{
        CHECK(getScore(1) == 50);
        CHECK(getScore(2) == 150);
        CHECK(getScore(3) == 300);
    }
}
