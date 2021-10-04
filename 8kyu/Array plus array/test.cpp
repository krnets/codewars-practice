#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ArrayPlusArray")
{
	using V = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(arrayPlusArray(V{1, 2, 3}, V{4, 5, 6}) == 21);
		CHECK(arrayPlusArray(V{1, -2, -3}, V{4, -5, 6}) == 1);
		CHECK(arrayPlusArray(V{-1, -2, -3}, V{-4, -5, -6}) == -21);
		CHECK(arrayPlusArray(V{0, 0, 0}, V{4, 5, 6}) == 15);
		CHECK(arrayPlusArray(V{-1}, V{-1}) == -2);
	}
}
