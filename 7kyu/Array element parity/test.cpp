#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Array_Element_Parity")
{
	using VI = std::vector<int>;

	SUBCASE("Example_tests")
	{
		CHECK(solve(VI{1,-1,2,-2,3}) == 3);
		CHECK(solve(VI{-3,1,2,3,-1,-4,-2}) == -4);
		CHECK(solve(VI{1,-1,2,-2,3,3}) == 3);
		CHECK(solve(VI {-110,110,-38,-38,-62,62,-38,-38,-38}) == -38);
		CHECK(solve(VI{-9,-105,-9,-9,-9,-9,105}) == -9);
	}
}
