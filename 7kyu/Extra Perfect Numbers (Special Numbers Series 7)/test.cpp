#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Extra_Perfect_Numbers")
{
	using vec = std::vector<int>;

	SUBCASE("Check_Small_Positive_Values")
	{
		CHECK(extraPerfect(3) == vec{1, 3}) ;
		CHECK(extraPerfect(5) == vec{1, 3, 5}) ;
		CHECK(extraPerfect(7) == vec{1, 3, 5, 7}) ;
	}
	SUBCASE("Check_Larger_Positive_Values")
	{
		CHECK(extraPerfect(28) == vec{1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27}) ;
		CHECK(extraPerfect(39) == vec{ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39 }) ;
	}
}
