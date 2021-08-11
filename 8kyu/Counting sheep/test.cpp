#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing count_sheep_method")
{
	SUBCASE("array_one")
	{
		std::vector<bool> array1 = {
			true, true, true, false,
			true, true, true, true,
			true, false, true, false,
			true, false, false, true,
			true, true, true, true,
			false, false, true, true
		};
		CHECK(count_sheep(array1) == 17);
	}
}
