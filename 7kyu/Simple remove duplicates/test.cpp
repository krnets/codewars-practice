#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Simple_Remove_Duplicates")
{
	using VI = std::vector<int>;

	SUBCASE("Example_tests")
	{
		CHECK(solve(VI{3,4,4,3,6,3}) == VI{4, 6, 3});
		CHECK(solve(VI{1,2,1,2,1,2,3}) == VI{1, 2, 3});
		CHECK(solve(VI{1,2,3,4}) == VI{1, 2, 3, 4});
		CHECK(solve(VI{1,1,4,5,1,2,1}) == VI{4, 5, 2, 1});
	}
}
