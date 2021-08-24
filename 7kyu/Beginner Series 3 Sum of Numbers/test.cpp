#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.h"

TEST_CASE("testing get_sum")
{
	SUBCASE("sample tests")
	{
		CHECK(get_sum(-1,2) == 2);
		CHECK(get_sum(0,-1) == -1);
		CHECK(get_sum(0,1) == 1);
		CHECK(get_sum(1,1) == 1);
		CHECK(get_sum(1,2) == 3);
	}
}
