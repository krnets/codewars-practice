#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing next prime")
{
	SUBCASE("sample tests")
	{
		CHECK(nextPrime(0) == 2);
		CHECK(nextPrime(2) == 3);
		CHECK(nextPrime(3) == 5);
		CHECK(nextPrime(5) == 7);
		CHECK(nextPrime(11) == 13);
		CHECK(nextPrime(13) == 17);
		CHECK(nextPrime(17) == 19);
		CHECK(nextPrime(23) == 29);
	}
}
