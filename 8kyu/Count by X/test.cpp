#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../../doctest.h"
#include "solve.cpp"
#include <vector>

TEST_CASE("testing Count_By_X")
{
	SUBCASE("Basic_Tests")
	{
		std::vector<int> expected = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		CHECK(countBy(1,10) == expected);

		expected = {2, 4, 6, 8, 10};
		CHECK(countBy(2,5) == expected);

		expected = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		CHECK(countBy(1,10) == expected);

		expected = {100, 200, 300, 400, 500};
		CHECK(countBy(100,5) == expected);
	}
}
