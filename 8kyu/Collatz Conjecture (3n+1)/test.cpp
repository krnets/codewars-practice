#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing collatz conjecture")
{
	SUBCASE("sample tests")
	{
		CHECK(hotpo(1) == 0);
		CHECK(hotpo(5) == 5);
		CHECK(hotpo(6) == 8);
		CHECK(hotpo(23) == 15);
	}
}
