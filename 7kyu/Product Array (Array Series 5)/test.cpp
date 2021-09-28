#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Product_Array")
{
	using vec = std::vector<int>;

	SUBCASE("Test_Small_Array_Size")
	{
		CHECK(productArray(vec{12, 20}) == vec{20, 12});
		CHECK(productArray(vec{1, 5, 2}) == vec{10, 2, 5});
		CHECK(productArray(vec{3, 27, 4, 2}) == vec{216, 24, 162, 324});
	}
	SUBCASE("Test_Larger_Array_Size")
	{
		CHECK(productArray(vec{13, 10, 5, 2, 9}) == vec{900, 1170, 2340, 5850, 1300});
		CHECK(productArray(vec{16, 17, 4, 3, 5, 2}) == vec{2040, 1920, 8160, 10880, 6528, 16320});
	}
}
