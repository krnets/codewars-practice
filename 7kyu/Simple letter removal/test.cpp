#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

void doTest(const string& s, unsigned k, const string& expected)
{
	CHECK(solve(s, k) == expected);
}

TEST_CASE("testing Sample_Tests")
{
	SUBCASE("Basic_Tests")
	{
		doTest("abracadabra", 1, "bracadabra");
		doTest("abracadabra", 2, "brcadabra");
		doTest("abracadabra", 6, "rcdbr");
		doTest("abracadabra", 8, "rdr");
		doTest("abracadabra", 50, "");
	}
}
