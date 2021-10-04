#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "solve.h"

TEST_CASE("testing ExampleTests")
{
	SUBCASE("BasicTests")
	{
		std::vector<int> expected = {0, 1};
		std::vector<int> actual = testit({0}, {1});
		CHECK(actual == expected);

		expected = {1, 2, 3, 4};
		actual = testit({1, 2}, {3, 4});
		CHECK(actual == expected);

		expected = {1, 2, 3, 4};
		actual = testit({1}, {2, 3, 4});
		CHECK(actual == expected);

		expected = {1, 2, 3, 4};
		actual = testit({1, 2, 3}, {4});
		CHECK(actual == expected);

		expected = {1, 1, 2, 2};
		actual = testit({1, 2}, {1, 2});
		CHECK(actual == expected);

		expected = {1, 1, 2, 2};
		actual = testit({1, 2, 2, 2, 2}, {1, 2});
		CHECK(actual == expected);
	}
}
