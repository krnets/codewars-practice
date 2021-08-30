#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing AlphabetWar")
{
	SUBCASE("BasicTest")
	{
		CHECK(alphabetWar("z") == "Right side wins!");
		CHECK(alphabetWar("zdqmwpbs") == "Let's fight again!");
		CHECK(alphabetWar("zzzzs") == "Right side wins!");
		CHECK(alphabetWar("wwwwww") == "Left side wins!");
		CHECK(alphabetWar("zb") == "Left side wins!");
		CHECK(alphabetWar("p") == "Left side wins!");
	}
}
