#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing HasUniqueChars")
{
	SUBCASE("BasicTests")
	{
		CHECK(hasUniqueChars("  nAa") == false);
		CHECK(hasUniqueChars("abcdef") == true);
		CHECK(hasUniqueChars("++-") == false);
		CHECK(hasUniqueChars(" nAa ") == false);
		CHECK(hasUniqueChars("") == true);
	}
}
