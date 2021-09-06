#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Sum_of_array_singles")
{
	SUBCASE("Example_tests")
	{
		using VI = std::vector<int>;
		// CHECK(repeats(VI{4,5,7,5,4,8}) == 15);
		// CHECK(repeats(VI{9, 10, 19, 13, 19, 13}) == 19);
		CHECK(repeats(VI{16, 0, 11, 4, 8, 16, 0, 11}) == 12);
		// CHECK(repeats(VI{5, 17, 18, 11, 13, 18, 11, 13}) == 22);
	}
}
