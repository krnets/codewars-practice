#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Example_from_description")
{
	SUBCASE("Beattles")
	{
		CHECK(decodeMorse(".... . -.--   .--- ..- -.. .") == "HEY JUDE");
	}
}
