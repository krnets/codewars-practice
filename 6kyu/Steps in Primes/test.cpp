#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void dotest(int g, long long m, long long n, std::pair<long long, long long> expected)
{
	CHECK(StepInPrimes::step(g, m, n) == expected);
}

TEST_CASE("testing step_Tests")
{
	SUBCASE("Fixed_Tests")
	{
		dotest(2, 100, 110, {101, 103});
		dotest(11, 30000, 100000, {0, 0});
		dotest(2, 2, 50, {3, 5});
		dotest(4, 100, 110, {103, 107});
		dotest(6, 100, 110, {101, 107});
		dotest(8, 300, 400, {359, 367});
		dotest(10, 300, 400, {307, 317});
	}
}
