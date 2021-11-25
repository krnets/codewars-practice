#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing HelloWorld")
{
	SUBCASE("BasicTest")
	{
		CHECK_EQ(f(), "Hello, world!");
	}
}
