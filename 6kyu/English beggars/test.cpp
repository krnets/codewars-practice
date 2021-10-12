#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Beggars")
{
	using V = std::vector<int>;
	SUBCASE("BasicTests")
	{
    CHECK(beggars(V{1,2,3,4,5},1) == V{15});
    CHECK(beggars(V{1,2,3,4,5},2) == V{9,6});
    CHECK(beggars(V{1,2,3,4,5},3) == V{5,7,3});
    CHECK(beggars(V{1,2,3,4,5},6) == V{1,2,3,4,5,0});
    CHECK(beggars(V{1,2,3,4,5},0) == V{});
  }
}
