#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing invite_more_women")
{
	SUBCASE("Sample_Tests")
	{
		CHECK(invite_more_women({1, -1, 1}) == true);
		CHECK(invite_more_women({-1, -1, -1}) == false);
		CHECK(invite_more_women({1, -1}) == false);
		CHECK(invite_more_women({1, 1, 1}) == true);
	}
}
