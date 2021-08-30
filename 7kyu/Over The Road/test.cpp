#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing over_the_road")
{
	SUBCASE("Basic_Test_Cases")
	{
		CHECK(over_the_road(1, 3) == 6);
		CHECK(over_the_road(3, 3) == 4);
		CHECK(over_the_road(2, 3) == 5);

		CHECK(over_the_road(3, 5) == 8);

		CHECK(over_the_road(7, 11) == 16);
		CHECK(over_the_road(23633656673, 310027696726) == 596421736780);
	}
}
