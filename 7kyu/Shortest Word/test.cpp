#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing find_short")
{
	SUBCASE("Sample_Test_Cases")
	{
		CHECK(find_short("bitcoin take over the world maybe who knows perhaps") == 3);
		CHECK(find_short("turns out random test cases are easier than writing out basic ones") == 3);
		CHECK(find_short("lets talk about javascript the best language") == 3);
		CHECK(find_short("i want to travel the world writing code one day") == 1);
		CHECK(find_short("Lets all go on holiday somewhere very cold") == 2);
		CHECK(find_short("Let's travel abroad shall we") == 2);
	}
}
