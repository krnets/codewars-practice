#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing mod256WithoutMod")
{
	SUBCASE("basic_tests")
	{
		CHECK(mod256WithoutMod(254) == 254);
		CHECK(mod256WithoutMod(256) == 0);
		CHECK(mod256WithoutMod(258) == 2);

		CHECK(mod256WithoutMod(-254) == -254);
		CHECK(mod256WithoutMod(-256) == 0);
		CHECK(mod256WithoutMod(-258) == -2);
	}
}
