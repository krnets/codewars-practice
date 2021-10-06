#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing is_Prime")
{
	SUBCASE("Sample_Test")
	{
		CHECK(isPrime(-1) == false);
		CHECK(isPrime(1) == false);
		CHECK(isPrime(2) == true);
		CHECK(isPrime(3) == true);
		CHECK(isPrime(5) == true);
		CHECK(isPrime(50) == false);
	}
}
