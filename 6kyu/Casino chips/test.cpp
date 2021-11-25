#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Casino_chips")
{
	using VI = std::vector<int>;

	SUBCASE("Example_tests")
	{
		CHECK(solve(VI{1,1,1}) == 1);
		CHECK(solve(VI{1,2,1}) == 2);
		CHECK(solve(VI{4,1,1}) == 2);
		CHECK(solve(VI{8,2,8}) == 9);
		CHECK(solve(VI{8,1,4}) == 5);
		CHECK(solve(VI{7,4,10}) == 10);
		CHECK(solve(VI{12,12,12}) == 18);
		CHECK(solve(VI{1,23,2}) == 3);
	}
}
