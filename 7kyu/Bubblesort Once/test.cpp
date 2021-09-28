#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing Tests")
{
	SUBCASE("ExampleTest")
	{
		// Example test case from description
		std::vector<int> expected = {7, 5, 3, 1, 2, 4, 6, 8, 9};
		std::vector<int> actual = bubbleSortOnce({9, 7, 5, 3, 1, 2, 4, 6, 8});
		CHECK(actual == expected);
	}
}
