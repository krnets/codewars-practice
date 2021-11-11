#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void dotest(int g, long long m, long long n, std::pair<long long, long long> expected)
{
	CHECK(GapInPrimes::gap(g, m, n) == expected);
}

TEST_CASE("testing Gap in Primes")
{
	SUBCASE("Test 1")
	{
		dotest(2, 100, 110, {101, 103});
	}
	SUBCASE("Test 2")
	{
		dotest(4, 100, 110, {103, 107});
	}
	SUBCASE("Test 3")
	{
		dotest(6, 100, 110, {0, 0});
	}
	SUBCASE("Test 4")
	{
		dotest(8, 300, 400, {359, 367});
	}
	SUBCASE("Test 5")
	{
		dotest(10, 300, 400, {337, 347});
	}
}
