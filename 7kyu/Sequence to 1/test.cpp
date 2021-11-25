#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing SeqToOne")
{
	SUBCASE("Decreasing")
	{
		CHECK_EQ(seqToOne(5), vector{5, 4, 3, 2, 1});
	}
	SUBCASE("Increasing")
	{
		CHECK_EQ(seqToOne(-1), vector{-1, 0, 1});
	}
}
