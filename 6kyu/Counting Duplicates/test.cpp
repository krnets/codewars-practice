#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing sample_Tests")
{
	SUBCASE("small_Tests")
	{
		CHECK(duplicateCount(" ") == 0);
		CHECK(duplicateCount("") == 0);
		CHECK(duplicateCount("asdfghjkl;'\\") == 0);
		CHECK(duplicateCount("asdfghjkl;'\\'") == 1);
		CHECK(duplicateCount("aabbcde") == 2);
		CHECK(duplicateCount("aabBcde") == 2);
		CHECK(duplicateCount("Indivisibility") == 1);
		CHECK(duplicateCount("Indivisibilities") == 2);
		CHECK(duplicateCount("ABBA") == 2);
	}
}
