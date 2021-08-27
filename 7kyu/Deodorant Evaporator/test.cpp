#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing evaporator")
{
	SUBCASE("sample tests")
	{
		CHECK(Evaporator::evaporator(10, 10, 10) == 22);
		CHECK(Evaporator::evaporator(10, 10, 5) == 29);
	}
}
