#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing bingo")
{
	using p = std::pair<std::string, int>;

	SUBCASE("Example_tests")
	{
		CHECK(bingo({p("ABC", 65), p("HGR", 74), p("BYHT", 74)}, 2) == "Loser!");
		CHECK(bingo({p("ABC", 65), p("HGR", 74), p("BYHT", 74)}, 1) == "Winner!");
		CHECK(bingo({p("HGTYRE", 74), p("BE", 66), p("JKTY", 74)}, 3) == "Loser!");
	}
	SUBCASE("Failing")
	{
		CHECK(bingo({p("LVS", 65), p("UZY", 68), p("TPDRB", 90), p("DNPGTFO", 84), p("PDCAVZI", 88), p("THFHIWHP", 73),
			p( "PNVCELGK", 75),p("DCUJDGC", 66)}, 2) == "Winner!");
	}
}
