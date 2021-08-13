#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing min max")
{
	using V = std::vector<int>;

	SUBCASE("examples")
	{
		CHECK(min(V{-52, 56, 30, 29, -54, 0, -110} ) == -110);
		CHECK(min(V{42, 54, 65, 87, 0} ) == 0);
		CHECK(max(V{4,6,2,1,9,63,-134,566}) == 566);
		CHECK(max(V{5}) == 5);
	}
}
