#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Minimum_Value")
{
	SUBCASE("Check_Small_Vector_Size")
	{
		CHECK(minValue({1, 3, 1}) == 13);
		CHECK(minValue({4, 7, 5, 7}) == 457);
		CHECK(minValue({4, 8, 1, 4}) == 148);
		CHECK(minValue({5, 7, 9, 5, 7}) == 579);
		CHECK(minValue({6, 7, 8, 7, 6, 6}) == 678);
	}
	SUBCASE("Check_Larger_Vector_Size")
	{
		CHECK(minValue({5, 6, 9, 9, 7, 6, 4}) == 45679);
		CHECK(minValue({1, 9, 1, 3, 7, 4, 6, 6, 7}) == 134679);
		CHECK(minValue({3, 6, 5, 5, 9, 8, 7, 6, 3, 5, 9}) == 356789);
	}
}
