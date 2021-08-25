#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <random>
#include <doctest/doctest.h>
#include "solve.h"

auto randint(int min, int max)
{
	static std::random_device rd;
	static std::mt19937 rng(rd());
	std::uniform_int_distribution<int> uni(min, max);

	return uni(rng);
}

TEST_CASE("testing RowSumOddNumbers")
{
	SUBCASE("BasicTests")
	{
		CHECK(rowSumOddNumbers(1) == 1);
		CHECK(rowSumOddNumbers(2) == 8);
		CHECK(rowSumOddNumbers(3) == 27);
		CHECK(rowSumOddNumbers(4) == 64);
		CHECK(rowSumOddNumbers(5) == 125);
		CHECK(rowSumOddNumbers(42) == 74088);
	}

	SUBCASE("RandomTests")
	{
		for (unsigned int i = 0; i < 40; i++)
		{
			unsigned int n = randint(1, 200);
			CHECK(rowSumOddNumbers(n) == n * n * n);
		}
	}
}
