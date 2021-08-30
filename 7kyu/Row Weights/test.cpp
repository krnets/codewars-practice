#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Row_Weights")
{
	using vec = std::vector<int>;
	using p = std::pair<int, int>;

	SUBCASE("Basic_Tests")
	{
		CHECK(rowWeights(vec{80}) == p{80, 0});
		CHECK(rowWeights(vec{100, 50}) == p{100, 50});
		CHECK(rowWeights(vec{50, 60, 70, 80}) == p{120, 140});
	}
	SUBCASE("Odd_Vector_Length")
	{
		CHECK(rowWeights(vec{13, 27, 49}) == p{62, 27});
		CHECK(rowWeights(vec{70, 58, 75, 34, 91}) == p{236, 92});
		CHECK(rowWeights(vec{29, 83, 67, 53, 19, 28, 96}) == p{211, 164});
	}
	SUBCASE("Even_Vector_Length")
	{
		CHECK(rowWeights(vec{100, 50}) == p{100, 50});
		CHECK(rowWeights(vec{100, 51, 50, 100}) == p{150, 151});
		CHECK(rowWeights(vec{39, 84, 74, 18, 59, 72, 35, 61}) == p{207, 235});
	}
}
