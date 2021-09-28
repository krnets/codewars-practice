#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing String_matchup")
{
	using VI = vector<int>;
	using VS = vector<string>;

	SUBCASE("Example_tests")
	{
		CHECK(solve(VS{"abc", "abc", "xyz", "abcd", "cde"}, VS{"abc", "cde", "uap"}) == VI{2, 1, 0});
		CHECK(solve(VS{"abc", "xyz", "abc", "xyz", "cde"}, VS{"abc", "cde", "xyz"}) == VI{2, 1, 2});
	}
}
