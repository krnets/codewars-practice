#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing disemvowel")
{
	SUBCASE("sample tests")
	{
		CHECK(disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!");
		CHECK(disemvowel("No offense but,\nYour writing is among the worst I've ever read") ==
			"N ffns bt,\nYr wrtng s mng th wrst 'v vr rd");
		CHECK(disemvowel("What are you, a communist?") == "Wht r y,  cmmnst?");
	}
}
