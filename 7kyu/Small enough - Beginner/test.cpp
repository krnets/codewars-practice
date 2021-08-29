#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Fixed_tests")
{
	SUBCASE("Basic_cases")
	{
		CHECK(small_enough(std::vector<int>{66, 101}, 200) == true);
		CHECK(small_enough(std::vector<int>{78, 117, 110, 99, 104, 117, 107, 115}, 100) == false);
		CHECK(small_enough(std::vector<int>{101, 45, 75, 105, 99, 107}, 107) == true);
		CHECK(small_enough(std::vector<int>{80, 117, 115, 104, 45, 85, 112, 115}, 120) == true);
		CHECK(small_enough(std::vector<int>{1, 1, 1, 1, 1, 2}, 1) == false);
		CHECK(small_enough(std::vector<int>{78, 33, 22, 44, 88, 9, 6}, 87) == false);
		CHECK(small_enough(std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9}, 10) == true);
		CHECK(small_enough(std::vector<int>{12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12}, 12) == true);
	}
}
