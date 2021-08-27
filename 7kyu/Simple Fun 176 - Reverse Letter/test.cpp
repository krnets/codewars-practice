#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ")
{
	SUBCASE("basic_tests")
	{
		CHECK(reverse_letter("krishan") == "nahsirk");
		CHECK(reverse_letter("ultr53o?n") == "nortlu");
		CHECK(reverse_letter("ab23c") == "cba");
		CHECK(reverse_letter("krish21an") == "nahsirk");
	}
}
