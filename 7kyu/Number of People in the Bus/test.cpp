#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Number of people in the bus")
{
	using P = std::pair<int, int>;
	using V = std::vector<P>;

	SUBCASE("BasicTests")
	{
		CHECK(number(V{P{10,0},P{3,5},P{5,8}}) == 5);
		CHECK(number(V{P{3,0},P{9,1},P{4,10},P{12,2},P{6,1},P{7,10}}) == 17);
		CHECK(number(V{P{3,0},P{9,1},P{4,8},P{12,2},P{6,1},P{7,8}}) == 21);
		CHECK(number(V{P{0,0}}) == 0);
		CHECK(number(V{P{10,0},P{13,0},P{17,40}}) == 0);
	}
}
