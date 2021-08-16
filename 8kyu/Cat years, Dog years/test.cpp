#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"

TEST_CASE("testing HumanYearsCatYearsDogYears")
{
	using V = std::vector<int>;

	SUBCASE("BasicTests")
	{
		CHECK(humanYearsCatYearsDogYears( 1) == V{1, 15, 15});
		// CHECK(humanYearsCatYearsDogYears( 2) == V{2, 24, 24});
		// CHECK(humanYearsCatYearsDogYears(10) == V{10, 56, 64});
	}
}
