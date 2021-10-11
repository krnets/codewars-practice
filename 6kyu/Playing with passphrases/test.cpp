#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

static void dotest(std::string s, int n, std::string expected)
{
	CHECK(PlayPass::playPass(s, n) == expected);
}

TEST_CASE("testing playPass_Tests")
{
	SUBCASE("Fixed__Tests")
	{
		dotest("BORN IN 2015!", 1, "!4897 Oj oSpC");
		dotest("I LOVE YOU!!!", 1, "!!!vPz fWpM J");
		dotest("I LOVE YOU!!!", 0, "!!!uOy eVoL I");
		dotest("AAABBCCY", 1, "zDdCcBbB");
		dotest("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2,
		       "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO");
	}
}
