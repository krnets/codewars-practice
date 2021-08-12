#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing MonkeyCount")
{
	using vec = std::vector<int>;

	SUBCASE("Should Work For Fixed Tests")
	{
		CHECK(MonkeyCount(5) == vec{1, 2, 3, 4, 5});
		CHECK(MonkeyCount(3) == vec{1, 2, 3});
		CHECK(MonkeyCount(9) == vec{1, 2, 3, 4, 5, 6, 7, 8, 9}) ;
		CHECK(MonkeyCount(10) == vec{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) ;
		CHECK(MonkeyCount(20) == vec{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}) ;
	}
}
