#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing countSmileys")
{
	SUBCASE("Basic_testing")
	{
		CHECK(countSmileys({}) == 0);
		CHECK(countSmileys({":D", ":~)", ";~)", ":)"}) == 4);
		CHECK(countSmileys({":)", ":(", ":D", ":O", ":;"}) == 2);
		CHECK(countSmileys({";]", ":[", ";*", ":$", ";-D"}) == 1);
	}
}
